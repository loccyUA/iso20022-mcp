"""Tests for pactus.core.parsers.parse_pacs008."""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal

import pytest

from pactus.core.domain import ParsedPacs008
from pactus.core.parsers import parse_pacs008


class TestParsePacs008Single:
    """Parsing a pacs.008 message with one transaction."""

    def test_returns_parsed_pacs008(self, pacs008_single_xml: str) -> None:
        result = parse_pacs008(pacs008_single_xml)
        assert isinstance(result, ParsedPacs008)

    def test_group_header_has_message_id(self, pacs008_single_xml: str) -> None:
        result = parse_pacs008(pacs008_single_xml)
        assert result.group_header.message_id == "MSG20240508001"

    def test_group_header_creation_datetime_is_python_datetime(
        self, pacs008_single_xml: str
    ) -> None:
        result = parse_pacs008(pacs008_single_xml)
        assert isinstance(result.group_header.creation_datetime, datetime)

    def test_group_header_number_of_transactions_is_int(self, pacs008_single_xml: str) -> None:
        result = parse_pacs008(pacs008_single_xml)
        assert result.group_header.number_of_transactions == 1
        assert isinstance(result.group_header.number_of_transactions, int)

    def test_settlement_method_is_clean_string(self, pacs008_single_xml: str) -> None:
        result = parse_pacs008(pacs008_single_xml)
        assert result.group_header.settlement_method == "CLRG"

    def test_one_transaction(self, pacs008_single_xml: str) -> None:
        result = parse_pacs008(pacs008_single_xml)
        assert len(result.transactions) == 1

    def test_transaction_amount_is_decimal(self, pacs008_single_xml: str) -> None:
        result = parse_pacs008(pacs008_single_xml)
        amt = result.transactions[0].settlement_amount
        assert isinstance(amt.value, Decimal)
        assert amt.value == Decimal("1000.00")
        assert amt.currency == "USD"

    def test_charge_bearer_is_clean_string(self, pacs008_single_xml: str) -> None:
        result = parse_pacs008(pacs008_single_xml)
        assert result.transactions[0].charge_bearer == "SHAR"

    def test_party_names(self, pacs008_single_xml: str) -> None:
        result = parse_pacs008(pacs008_single_xml)
        tx = result.transactions[0]
        assert tx.debtor.name == "Acme Corporation"
        assert tx.creditor.name == "Global Supplies Ltd"

    def test_agent_bics_unwrapped_correctly(self, pacs008_single_xml: str) -> None:
        result = parse_pacs008(pacs008_single_xml)
        tx = result.transactions[0]
        assert tx.debtor_agent is not None
        assert tx.debtor_agent.bic == "CHASUS33"
        assert tx.creditor_agent is not None
        assert tx.creditor_agent.bic == "DEUTDEDB"


class TestParsePacs008Multi:
    """Parsing a pacs.008 message with multiple transactions."""

    def test_returns_three_transactions(self, pacs008_multi_xml: str) -> None:
        result = parse_pacs008(pacs008_multi_xml)
        assert len(result.transactions) == 3

    def test_transactions_preserve_order(self, pacs008_multi_xml: str) -> None:
        result = parse_pacs008(pacs008_multi_xml)
        assert [tx.end_to_end_id for tx in result.transactions] == ["E2E-001", "E2E-002", "E2E-003"]

    def test_distinct_amounts_and_currencies(self, pacs008_multi_xml: str) -> None:
        result = parse_pacs008(pacs008_multi_xml)
        amounts = [
            (tx.settlement_amount.value, tx.settlement_amount.currency)
            for tx in result.transactions
        ]
        assert amounts == [
            (Decimal("1500.00"), "EUR"),
            (Decimal("250.50"), "EUR"),
            (Decimal("9999.99"), "USD"),
        ]

    def test_distinct_charge_bearers(self, pacs008_multi_xml: str) -> None:
        result = parse_pacs008(pacs008_multi_xml)
        assert [tx.charge_bearer for tx in result.transactions] == ["SHAR", "DEBT", "CRED"]

    def test_remittance_info_extracted_when_present(self, pacs008_multi_xml: str) -> None:
        result = parse_pacs008(pacs008_multi_xml)
        assert result.transactions[1].remittance_info == "Invoice 2026-Q2-447"
        assert result.transactions[0].remittance_info is None


class TestParsePacs008Failures:
    """Failure modes of parse_pacs008."""

    def test_malformed_xml_raises(self) -> None:
        with pytest.raises(Exception):  # noqa: B017 — multiple exception classes possible
            parse_pacs008("<not-xml>")

    def test_wrong_message_type_raises_validation_error(self) -> None:
        # A valid XML but not a pacs.008 envelope.
        xml = '<?xml version="1.0"?><Document xmlns="urn:iso:std:iso:20022:tech:xsd:pain.001.001.09"/>'
        with pytest.raises(Exception):  # noqa: B017
            parse_pacs008(xml)


class TestSchemaExportableForLLM:
    """The whole point of the domain layer: clean JSON schemas for the LLM."""

    def test_parsed_pacs008_has_native_pydantic_schema(self) -> None:
        """If this raises, we leaked an xsdata XmlPeriod/XmlDate type into the domain model."""
        schema = ParsedPacs008.model_json_schema()
        assert "properties" in schema

    def test_charge_bearer_is_literal_enum_in_schema(self) -> None:
        schema = ParsedPacs008.model_json_schema()
        # The Literal type should appear as an enum constraint somewhere in the schema.
        import json

        schema_str = json.dumps(schema)
        assert "SHAR" in schema_str
        assert "DEBT" in schema_str

    def test_amount_value_serializes_as_string(self) -> None:
        """Decimals must serialize as strings, not floats, to preserve precision."""
        from pactus.core.domain.common import Amount

        amt = Amount(value=Decimal("123.45"), currency="USD")
        dumped = amt.model_dump(mode="json")
        assert isinstance(dumped["value"], str), (
            f"Decimal serialized as {type(dumped['value']).__name__}, expected str"
        )

    def test_amount_value_schema_has_no_lookaround_regex(self) -> None:
        """The MoneyDecimal type must produce an ECMA-262-compatible JSON schema.

        Pydantic's default Decimal schema uses negative look-ahead in its
        pattern, which strict MCP clients reject. MoneyDecimal sidesteps
        this by serializing as a plain string with no regex constraint.
        """
        import json

        schema_str = json.dumps(ParsedPacs008.model_json_schema())
        assert "(?!" not in schema_str, (
            "JSON schema contains look-around regex — MCP clients will reject it"
        )
        assert "(?<" not in schema_str, (
            "JSON schema contains look-behind regex — MCP clients will reject it"
        )

    def test_money_decimal_rejects_unsupported_type(self) -> None:
        """MoneyDecimal must reject types it can't safely coerce.

        Covers the ``raise TypeError`` branch in ``_coerce_to_decimal``.
        Pydantic propagates ``TypeError`` from a ``BeforeValidator`` rather
        than wrapping it in ``ValidationError``, so we accept either.
        """
        from pydantic import ValidationError

        from pactus.core.domain.common import Amount

        with pytest.raises((ValidationError, TypeError)):
            Amount(value={"not": "a number"}, currency="USD")  # type: ignore[arg-type]

    def test_money_decimal_coerces_string_input(self) -> None:
        """MoneyDecimal must accept string input and coerce to Decimal.

        Covers the str/int/float coercion branch in ``_coerce_to_decimal``.
        The parser only ever feeds in Decimal, so this is the only path
        that exercises the string-coercion line.
        """
        from pactus.core.domain.common import Amount

        amt = Amount(value="123.45", currency="USD")  # type: ignore[arg-type]
        assert amt.value == Decimal("123.45")


class TestParsePacs008OptionalFieldHandling:
    """Optional-field branches in parse_pacs008.

    These tests close the branch-coverage gaps surfaced when branch
    measurement was enabled.
    """

    def test_settlement_date_parsed_when_present(self) -> None:
        """When <IntrBkSttlmDt> is present, it must be projected as a date.

        Covers the ``tx.intr_bk_sttlm_dt is not None`` True branch in
        _project_transaction. Existing fixtures omit the field, so this
        is the only test that exercises the date-projection path.
        """
        from datetime import date

        xml = """<?xml version="1.0" encoding="UTF-8"?>
<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08">
  <FIToFICstmrCdtTrf>
    <GrpHdr>
      <MsgId>MSG-WITH-SETTLE-DATE</MsgId>
      <CreDtTm>2026-05-10T10:00:00</CreDtTm>
      <NbOfTxs>1</NbOfTxs>
      <SttlmInf><SttlmMtd>CLRG</SttlmMtd></SttlmInf>
    </GrpHdr>
    <CdtTrfTxInf>
      <PmtId><EndToEndId>E2E-WD-001</EndToEndId></PmtId>
      <IntrBkSttlmAmt Ccy="USD">100.00</IntrBkSttlmAmt>
      <IntrBkSttlmDt>2026-05-12</IntrBkSttlmDt>
      <ChrgBr>SHAR</ChrgBr>
      <Dbtr><Nm>Test Debtor</Nm></Dbtr>
      <DbtrAgt><FinInstnId><BICFI>CHASUS33</BICFI></FinInstnId></DbtrAgt>
      <CdtrAgt><FinInstnId><BICFI>DEUTDEDB</BICFI></FinInstnId></CdtrAgt>
      <Cdtr><Nm>Test Creditor</Nm></Cdtr>
    </CdtTrfTxInf>
  </FIToFICstmrCdtTrf>
</Document>"""
        result = parse_pacs008(xml)
        assert result.transactions[0].settlement_date == date(2026, 5, 12)

    def test_remittance_info_omitted_yields_none(self) -> None:
        """When <RmtInf> is absent, remittance_info must be None.

        Covers the ``tx.rmt_inf is not None`` False branch.
        """
        from tests.conftest import FIXTURES_DIR

        xml = (FIXTURES_DIR / "test_pacs008.xml").read_text(encoding="utf-8")
        result = parse_pacs008(xml)
        assert result.transactions[0].remittance_info is None
