import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from server import (
    convert_mt_to_mx,
    parse_camt053,
    parse_pacs008,
    parse_pain001,
    validate_camt053,
    validate_pacs008,
    validate_pain001,
)


def load(name: str) -> str:
    return (ROOT / name).read_text()


PACS008_NO_MSGID = """<?xml version="1.0"?>
<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08">
  <FIToFICstmrCdtTrf>
    <CdtTrfTxInf>
      <IntrBkSttlmAmt Ccy="USD">1000.00</IntrBkSttlmAmt>
      <Dbtr><Nm>Acme</Nm></Dbtr>
      <DbtrAgt><FinInstnId><BICFI>CHASUS33</BICFI></FinInstnId></DbtrAgt>
      <Cdtr><Nm>Globex</Nm></Cdtr>
      <CdtrAgt><FinInstnId><BICFI>DEUTDEDB</BICFI></FinInstnId></CdtrAgt>
    </CdtTrfTxInf>
  </FIToFICstmrCdtTrf>
</Document>"""

PAIN001_NO_MSGID = """<?xml version="1.0"?>
<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pain.001.001.09">
  <CstmrCdtTrfInitn>
    <GrpHdr>
      <NbOfTxs>1</NbOfTxs>
      <CtrlSum>100.00</CtrlSum>
    </GrpHdr>
    <PmtInf>
      <Dbtr><Nm>Acme</Nm></Dbtr>
      <DbtrAcct><Id><IBAN>DE89370400440532013000</IBAN></Id></DbtrAcct>
      <CdtTrfTxInf><Cdtr><Nm>Globex</Nm></Cdtr></CdtTrfTxInf>
    </PmtInf>
  </CstmrCdtTrfInitn>
</Document>"""

CAMT053_NO_IBAN = """<?xml version="1.0"?>
<Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.053.001.08">
  <BkToCstmrStmt>
    <GrpHdr><MsgId>CAMT-001</MsgId></GrpHdr>
    <Stmt>
      <Acct><Id></Id></Acct>
      <Bal>
        <Tp><CdOrPrtry><Cd>OPBD</Cd></CdOrPrtry></Tp>
        <Amt Ccy="EUR">100.00</Amt>
      </Bal>
    </Stmt>
  </BkToCstmrStmt>
</Document>"""

MALFORMED_XML = "not xml at all <<<"

MT103_NO_MSGID = """:23B:CRED
:32A:260508USD1000,00
:59:Global Supplies Ltd
"""

MT103_BAD_32A = """:20:TESTREF
:23B:CRED
:32A:INVALID-NOT-A-DATE
:59:Global Supplies Ltd
"""


# ---- convert_mt_to_mx ----

def test_convert_mt_to_mx_happy_path():
    result = convert_mt_to_mx(load("test_mt103.txt"))
    assert "error" not in result
    fm = result["field_mapping"]
    assert fm["20"]["value"] == "TRF-2026050800001"
    assert fm["32A"]["pacs008_field"] == "IntrBkSttlmDt + IntrBkSttlmAmt[Ccy]"
    assert fm["52A"]["value"] == "CHASUS33"
    # Roundtrip: generated XML must be parseable by the existing pacs.008 tool
    parsed = parse_pacs008(result["pacs008_xml"])
    assert parsed["message_id"] == "TRF-2026050800001"
    assert parsed["currency"] == "USD"
    assert parsed["amount"] == "1000.00"
    assert parsed["debtor"] == "Acme Corporation"
    assert parsed["debtor_bic"] == "CHASUS33"
    assert parsed["creditor"] == "Global Supplies Ltd"
    assert parsed["creditor_bic"] == "DEUTDEDB"


def test_convert_mt_to_mx_missing_mandatory():
    result = convert_mt_to_mx(MT103_NO_MSGID)
    assert "error" in result
    assert ":20:" in result["error"]


def test_convert_mt_to_mx_malformed_tag():
    result = convert_mt_to_mx(MT103_BAD_32A)
    assert "error" in result
    assert ":32A:" in result["error"]


# ---- pacs.008 ----

def test_parse_pacs008_happy_path():
    result = parse_pacs008(load("test_pacs008.xml"))
    assert result == {
        "message_id": "MSG20240508001",
        "amount": "1000.00",
        "currency": "USD",
        "debtor": "Acme Corporation",
        "debtor_bic": "CHASUS33",
        "creditor": "Global Supplies Ltd",
        "creditor_bic": "DEUTDEDB",
    }


def test_parse_pacs008_missing_field():
    result = parse_pacs008(PACS008_NO_MSGID)
    assert "error" in result
    assert "missing required field" in result["error"]


def test_validate_pacs008_happy_path():
    assert validate_pacs008(load("test_pacs008.xml")) == {"valid": True}


def test_validate_pacs008_missing_field():
    result = validate_pacs008(PACS008_NO_MSGID)
    assert result["valid"] is False
    assert "MsgId" in result["error"]


def test_validate_pacs008_malformed_xml():
    result = validate_pacs008(MALFORMED_XML)
    assert result["valid"] is False
    assert "parse error" in result["error"]


# ---- pain.001 ----

def test_parse_pain001_happy_path():
    result = parse_pain001(load("test_pain001.xml"))
    assert result == {
        "message_id": "PAIN001-20260508-001",
        "number_of_transactions": "2",
        "control_sum": "3500.00",
        "debtor": "Acme GmbH",
        "debtor_iban": "DE89370400440532013000",
        "creditor": "Globex SA",
    }


def test_parse_pain001_missing_field():
    result = parse_pain001(PAIN001_NO_MSGID)
    assert "error" in result
    assert "missing required field" in result["error"]


def test_validate_pain001_happy_path():
    assert validate_pain001(load("test_pain001.xml")) == {"valid": True}


def test_validate_pain001_missing_field():
    result = validate_pain001(PAIN001_NO_MSGID)
    assert result["valid"] is False
    assert "MsgId" in result["error"]


def test_validate_pain001_malformed_xml():
    result = validate_pain001(MALFORMED_XML)
    assert result["valid"] is False
    assert "parse error" in result["error"]


# ---- camt.053 ----

def test_parse_camt053_happy_path():
    result = parse_camt053(load("test_camt053.xml"))
    assert result == {
        "message_id": "CAMT053-20260508-001",
        "account_iban": "DE89370400440532013000",
        "opening_balance": {"amount": "10000.00", "currency": "EUR"},
        "closing_balance": {"amount": "8750.50", "currency": "EUR"},
        "number_of_entries": "2",
    }


def test_parse_camt053_missing_field():
    result = parse_camt053(CAMT053_NO_IBAN)
    assert "error" in result
    assert "missing required field" in result["error"]


def test_validate_camt053_happy_path():
    assert validate_camt053(load("test_camt053.xml")) == {"valid": True}


def test_validate_camt053_missing_field():
    result = validate_camt053(CAMT053_NO_IBAN)
    assert result["valid"] is False
    assert "IBAN" in result["error"]


def test_validate_camt053_malformed_xml():
    result = validate_camt053(MALFORMED_XML)
    assert result["valid"] is False
    assert "parse error" in result["error"]
