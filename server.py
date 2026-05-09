import logging
import re
import xml.etree.ElementTree as ET
from typing import Any

from fastmcp import FastMCP
from knowledge_base import query as kb_query

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
logger = logging.getLogger("iso20022-mcp")

mcp = FastMCP("iso20022-mcp")

PACS008_NS = {"iso": "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08"}
PAIN001_NS = {"iso": "urn:iso:std:iso:20022:tech:xsd:pain.001.001.09"}
CAMT053_NS = {"iso": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08"}

_MSGID_RE = re.compile(r"<(?:[^:>\s]+:)?MsgId\b[^>]*>([^<]+)</")

# MT103 → pacs.008 helpers
_MT_BLOCK4_RE = re.compile(r"\{4:(.*?)-\}", re.DOTALL)
_MT_TAG_RE = re.compile(r":(\d{2}[A-Z]?):(.*?)(?=:\d{2}[A-Z]?:|$)", re.DOTALL)
_MT32A_RE = re.compile(r"^(\d{6})([A-Z]{3})([\d,]+)$")
_MT33B_RE = re.compile(r"^([A-Z]{3})([\d,]+)$")
_MT103_MANDATORY = {"20", "23B", "32A", "59"}
_MT103_TAG_MAP = {
  "20": "GrpHdr/MsgId",
  "23B": "SvcLvl/Cd",
  "32A": "IntrBkSttlmDt + IntrBkSttlmAmt[Ccy]",
  "33B": "InstdAmt[Ccy]",
  "50K": "Dbtr/Nm",
  "52A": "DbtrAgt/FinInstnId/BICFI",
  "57A": "CdtrAgt/FinInstnId/BICFI",
  "59": "Cdtr/Nm",
  "70": "RmtInf/Ustrd",
  "71A": "ChrgBr",
}
_CHRGBR_MAP = {"OUR": "DEBT", "BEN": "CRED", "SHA": "SHAR"}
_PACS008_URI = "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08"


def _parse_mt103_tags(text: str) -> dict[str, str]:
  tags: dict[str, list[str]] = {}
  current: str | None = None
  for line in text.splitlines():
    m = re.match(r":(\d{2}[A-Z]?):(.*)", line)
    if m:
      current = m.group(1)
      tags[current] = [m.group(2)]
    elif current is not None:
      tags[current].append(line)
  return {tag: "\n".join(lines).strip() for tag, lines in tags.items()}


def _mt_account_and_name(raw: str) -> tuple[str | None, str]:
  iban = None
  name = ""
  iban_consumed = False
  for line in raw.splitlines():
    line = line.strip()
    if not line:
      continue
    if not iban_consumed and line.startswith("/"):
      account = line[1:].strip()
      space = account.find(" ")
      if space != -1:
        iban = account[:space] or None
        name = account[space + 1:].strip()
        return iban, name
      iban = account or None
      iban_consumed = True
      continue
    name = line
    break
  return iban, name


def _mt_amount(raw: str) -> str:
  return raw.replace(",", ".")


def _mt_date(yymmdd: str) -> str:
  return f"20{yymmdd[:2]}-{yymmdd[2:4]}-{yymmdd[4:6]}"


def _empty(xml: str) -> bool:
  return not xml or not xml.strip()


def _log_call(tool: str, xml: str) -> None:
  if not xml:
    logger.info("tool=%s input_preview=''", tool)
    return
  m = _MSGID_RE.search(xml)
  if m:
    logger.info("tool=%s message_id=%s", tool, m.group(1).strip())
  else:
    logger.info("tool=%s input_preview=%r", tool, xml[:50])


@mcp.tool()
def parse_pacs008(xml: str) -> dict[str, Any]:
  """Parse a pacs.008 (FIToFICustomerCreditTransfer) ISO 20022 message.

  Input: XML string in namespace urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08.
  Output: dict with keys message_id, amount, currency, debtor, debtor_bic, creditor,
          creditor_bic; or {"error": "..."} on failure.
  """
  _log_call("parse_pacs008", xml)
  if _empty(xml):
    return {"error": "empty input"}
  try:
    root = ET.fromstring(xml)
    return {
      "message_id": root.find(".//iso:MsgId", PACS008_NS).text,
      "amount": root.find(".//iso:IntrBkSttlmAmt", PACS008_NS).text,
      "currency": root.find(".//iso:IntrBkSttlmAmt", PACS008_NS).attrib["Ccy"],
      "debtor": root.find(".//iso:Dbtr/iso:Nm", PACS008_NS).text,
      "debtor_bic": root.find(".//iso:DbtrAgt//iso:BICFI", PACS008_NS).text,
      "creditor": root.find(".//iso:Cdtr/iso:Nm", PACS008_NS).text,
      "creditor_bic": root.find(".//iso:CdtrAgt//iso:BICFI", PACS008_NS).text,
    }
  except ET.ParseError as e:
    return {"error": f"XML parse error: {e}"}
  except AttributeError:
    return {"error": "missing required field"}


@mcp.tool()
def validate_pacs008(xml: str) -> dict[str, Any]:
  """Validate a pacs.008 ISO 20022 message.

  Input: XML string in namespace urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08.
  Output: {"valid": True} if required fields are present; otherwise
          {"valid": False, "error": "..."}; or {"error": "..."} for empty input.
  """
  _log_call("validate_pacs008", xml)
  if _empty(xml):
    return {"error": "empty input"}
  try:
    root = ET.fromstring(xml)
    required = [".//iso:MsgId", ".//iso:IntrBkSttlmAmt", ".//iso:Dbtr/iso:Nm",
                ".//iso:DbtrAgt//iso:BICFI", ".//iso:Cdtr/iso:Nm", ".//iso:CdtrAgt//iso:BICFI"]
    for path in required:
      if root.find(path, PACS008_NS) is None:
        return {"valid": False, "error": f"missing required element: {path}"}
    if "Ccy" not in root.find(".//iso:IntrBkSttlmAmt", PACS008_NS).attrib:
      return {"valid": False, "error": "missing Ccy attribute on IntrBkSttlmAmt"}
    return {"valid": True}
  except ET.ParseError as e:
    return {"valid": False, "error": f"XML parse error: {e}"}


@mcp.tool()
def parse_pain001(xml: str) -> dict[str, Any]:
  """Parse a pain.001 (CustomerCreditTransferInitiation) ISO 20022 message.

  Input: XML string in namespace urn:iso:std:iso:20022:tech:xsd:pain.001.001.09.
  Output: dict with keys message_id, number_of_transactions, control_sum, debtor,
          debtor_iban, creditor; or {"error": "..."} on failure.
  """
  _log_call("parse_pain001", xml)
  if _empty(xml):
    return {"error": "empty input"}
  try:
    root = ET.fromstring(xml)
    return {
      "message_id": root.find(".//iso:GrpHdr/iso:MsgId", PAIN001_NS).text,
      "number_of_transactions": root.find(".//iso:GrpHdr/iso:NbOfTxs", PAIN001_NS).text,
      "control_sum": root.find(".//iso:GrpHdr/iso:CtrlSum", PAIN001_NS).text,
      "debtor": root.find(".//iso:Dbtr/iso:Nm", PAIN001_NS).text,
      "debtor_iban": root.find(".//iso:DbtrAcct/iso:Id/iso:IBAN", PAIN001_NS).text,
      "creditor": root.find(".//iso:CdtTrfTxInf/iso:Cdtr/iso:Nm", PAIN001_NS).text,
    }
  except ET.ParseError as e:
    return {"error": f"XML parse error: {e}"}
  except AttributeError:
    return {"error": "missing required field"}


@mcp.tool()
def validate_pain001(xml: str) -> dict[str, Any]:
  """Validate a pain.001 ISO 20022 message.

  Input: XML string in namespace urn:iso:std:iso:20022:tech:xsd:pain.001.001.09.
  Output: {"valid": True} if required fields are present; otherwise
          {"valid": False, "error": "..."}; or {"error": "..."} for empty input.
  """
  _log_call("validate_pain001", xml)
  if _empty(xml):
    return {"error": "empty input"}
  try:
    root = ET.fromstring(xml)
    required = [".//iso:GrpHdr/iso:MsgId", ".//iso:GrpHdr/iso:NbOfTxs", ".//iso:GrpHdr/iso:CtrlSum",
                ".//iso:Dbtr/iso:Nm", ".//iso:DbtrAcct/iso:Id/iso:IBAN", ".//iso:CdtTrfTxInf/iso:Cdtr/iso:Nm"]
    for path in required:
      if root.find(path, PAIN001_NS) is None:
        return {"valid": False, "error": f"missing required element: {path}"}
    return {"valid": True}
  except ET.ParseError as e:
    return {"valid": False, "error": f"XML parse error: {e}"}


@mcp.tool()
def parse_camt053(xml: str) -> dict[str, Any]:
  """Parse a camt.053 (BankToCustomerStatement) ISO 20022 message.

  Input: XML string in namespace urn:iso:std:iso:20022:tech:xsd:camt.053.001.08.
  Output: dict with keys message_id, account_iban, opening_balance, closing_balance,
          number_of_entries; opening_balance and closing_balance are
          {"amount": str, "currency": str} or None; or {"error": "..."} on failure.
  """
  _log_call("parse_camt053", xml)
  if _empty(xml):
    return {"error": "empty input"}
  try:
    root = ET.fromstring(xml)

    def balance_for(code: str) -> dict[str, str] | None:
      for bal in root.findall(".//iso:Stmt/iso:Bal", CAMT053_NS):
        cd = bal.find("./iso:Tp/iso:CdOrPrtry/iso:Cd", CAMT053_NS)
        if cd is not None and cd.text == code:
          amt = bal.find("./iso:Amt", CAMT053_NS)
          return {"amount": amt.text, "currency": amt.attrib["Ccy"]}
      return None

    return {
      "message_id": root.find(".//iso:GrpHdr/iso:MsgId", CAMT053_NS).text,
      "account_iban": root.find(".//iso:Stmt/iso:Acct/iso:Id/iso:IBAN", CAMT053_NS).text,
      "opening_balance": balance_for("OPBD"),
      "closing_balance": balance_for("CLBD"),
      "number_of_entries": root.find(".//iso:Stmt/iso:TxsSummry/iso:TtlNtries/iso:NbOfNtries", CAMT053_NS).text,
    }
  except ET.ParseError as e:
    return {"error": f"XML parse error: {e}"}
  except AttributeError:
    return {"error": "missing required field"}


@mcp.tool()
def validate_camt053(xml: str) -> dict[str, Any]:
  """Validate a camt.053 ISO 20022 message.

  Input: XML string in namespace urn:iso:std:iso:20022:tech:xsd:camt.053.001.08.
  Output: {"valid": True} if required fields and at least one Bal entry are present;
          otherwise {"valid": False, "error": "..."}; or {"error": "..."} for empty input.
  """
  _log_call("validate_camt053", xml)
  if _empty(xml):
    return {"error": "empty input"}
  try:
    root = ET.fromstring(xml)
    required = [".//iso:GrpHdr/iso:MsgId", ".//iso:Stmt/iso:Acct/iso:Id/iso:IBAN"]
    for path in required:
      if root.find(path, CAMT053_NS) is None:
        return {"valid": False, "error": f"missing required element: {path}"}
    if not root.findall(".//iso:Stmt/iso:Bal", CAMT053_NS):
      return {"valid": False, "error": "missing required element: at least one Stmt/Bal"}
    return {"valid": True}
  except ET.ParseError as e:
    return {"valid": False, "error": f"XML parse error: {e}"}


@mcp.tool()
def explain_iso20022(question: str) -> dict[str, Any]:
  """Answer a question about ISO 20022 using the built-in knowledge base.

  Input: a natural-language question about ISO 20022 concepts, message types, or fields.
  Output: {"answer": str, "sources": list[str]} with the top matching knowledge chunks
          and their topic labels; or {"error": "..."} on empty input.
  """
  _log_call("explain_iso20022", question)
  if _empty(question):
    return {"error": "empty input"}
  hits = kb_query(question, n_results=3)
  return {
    "answer": "\n\n".join(h["text"] for h in hits),
    "sources": [h["topic"] for h in hits],
  }


@mcp.tool()
def convert_mt_to_mx(mt103: str) -> dict[str, Any]:
  """Convert an MT103 SWIFT message string to a pacs.008 ISO 20022 XML message.

  Input: MT103 SWIFT message string (with or without SWIFT block headers).
  Output: dict with keys field_mapping (MT103 tag → pacs.008 field name and parsed value)
          and pacs008_xml (a valid pacs.008 XML string);
          or {"error": "..."} on empty input, missing mandatory tags, or malformed values.
  """
  _log_call("convert_mt_to_mx", mt103)
  if _empty(mt103):
    return {"error": "empty input"}

  block4 = _MT_BLOCK4_RE.search(mt103)
  body = block4.group(1) if block4 else mt103
  tags = _parse_mt103_tags(body)

  for tag in _MT103_MANDATORY:
    if tag not in tags:
      return {"error": f"missing mandatory tag: :{tag}:"}

  m32a = _MT32A_RE.match(tags["32A"])
  if not m32a:
    return {"error": "malformed tag :32A:: expected YYMMDDCCCAMOUNT (e.g. 260508USD1000,00)"}

  sttlm_date = _mt_date(m32a.group(1))
  currency = m32a.group(2)
  amount = _mt_amount(m32a.group(3))

  instd_ccy = instd_amt = None
  if "33B" in tags:
    m33b = _MT33B_RE.match(tags["33B"])
    if not m33b:
      return {"error": "malformed tag :33B:: expected CCCAMOUNT (e.g. USD1000,00)"}
    instd_ccy, instd_amt = m33b.group(1), _mt_amount(m33b.group(2))

  dbtr_iban, dbtr_name = _mt_account_and_name(tags.get("50K", ""))
  cdtr_iban, cdtr_name = _mt_account_and_name(tags["59"])
  chrg_br = _CHRGBR_MAP.get(tags.get("71A", ""), "SHAR")
  dbtr_bic = tags.get("52A", "")
  cdtr_bic = tags.get("57A", "")
  rmt_info = tags.get("70", "")

  field_mapping = {
    tag: {"pacs008_field": _MT103_TAG_MAP[tag], "value": tags[tag]}
    for tag in _MT103_TAG_MAP
    if tag in tags
  }

  ET.register_namespace("", _PACS008_URI)
  ns = _PACS008_URI

  def el(parent, local):
    return ET.SubElement(parent, f"{{{ns}}}{local}")

  doc = ET.Element(f"{{{ns}}}Document")
  fi = el(doc, "FIToFICstmrCdtTrf")

  grp = el(fi, "GrpHdr")
  el(grp, "MsgId").text = tags["20"]
  el(grp, "CreDtTm").text = f"{sttlm_date}T00:00:00"
  el(grp, "NbOfTxs").text = "1"
  el(el(grp, "SttlmInf"), "SttlmMtd").text = "CLRG"

  cdt = el(fi, "CdtTrfTxInf")
  pmt_id = el(cdt, "PmtId")
  el(pmt_id, "InstrId").text = tags["20"]
  el(pmt_id, "EndToEndId").text = tags["20"]

  amt_el = el(cdt, "IntrBkSttlmAmt")
  amt_el.text = amount
  amt_el.set("Ccy", currency)
  el(cdt, "IntrBkSttlmDt").text = sttlm_date

  if instd_ccy:
    ia = el(cdt, "InstdAmt")
    ia.text = instd_amt
    ia.set("Ccy", instd_ccy)

  el(cdt, "ChrgBr").text = chrg_br

  if dbtr_bic:
    dbtr_agt = el(cdt, "DbtrAgt")
    el(el(dbtr_agt, "FinInstnId"), "BICFI").text = dbtr_bic

  el(el(cdt, "Dbtr"), "Nm").text = dbtr_name

  if dbtr_iban:
    el(el(el(cdt, "DbtrAcct"), "Id"), "IBAN").text = dbtr_iban

  if cdtr_bic:
    cdtr_agt = el(cdt, "CdtrAgt")
    el(el(cdtr_agt, "FinInstnId"), "BICFI").text = cdtr_bic

  el(el(cdt, "Cdtr"), "Nm").text = cdtr_name

  if cdtr_iban:
    el(el(el(cdt, "CdtrAcct"), "Id"), "IBAN").text = cdtr_iban

  if rmt_info:
    el(el(cdt, "RmtInf"), "Ustrd").text = rmt_info

  ET.indent(doc, space="  ")
  pacs008_xml = f'<?xml version="1.0" encoding="UTF-8"?>\n{ET.tostring(doc, encoding="unicode")}'

  return {"field_mapping": field_mapping, "pacs008_xml": pacs008_xml}


if __name__ == "__main__":
  mcp.run()
