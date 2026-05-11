"""Tests for camt.053.001.08 parsing.

camt.053 is the deepest hierarchy: GroupHeader → Statement[] → Balance[] +
Entry[] → EntryDetails[] → TransactionDetails[]. Tests cover the full
projection chain, optional-field omission, multi-balance scenarios, batched
entries, and the MCP error-handling wrapper.
"""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal

import pytest

from pactus.core.parsers import UnsafeXmlError, parse_camt053


class TestParseCamt053GroupHeader:
    """Group-header fields are extracted from the message-level GrpHdr."""

    def test_parses_message_id(self, camt053_single_xml: str) -> None:
        result = parse_camt053(camt053_single_xml)
        assert result.group_header.message_id == "CAMT053-SINGLE-001"

    def test_parses_creation_datetime(self, camt053_single_xml: str) -> None:
        result = parse_camt053(camt053_single_xml)
        assert isinstance(result.group_header.creation_datetime, datetime)
        assert result.group_header.creation_datetime == datetime(2026, 5, 10, 8, 0, 0)

    def test_statements_list_not_empty(self, camt053_single_xml: str) -> None:
        result = parse_camt053(camt053_single_xml)
        assert len(result.statements) == 1


class TestParseCamt053Statement:
    """Statement-level fields: id, dates, account, balances, entries."""

    def test_statement_id(self, camt053_single_xml: str) -> None:
        stmt = parse_camt053(camt053_single_xml).statements[0]
        assert stmt.statement_id == "STMT-2026-05-09-001"

    def test_statement_creation_datetime_optional(self, camt053_single_xml: str) -> None:
        stmt = parse_camt053(camt053_single_xml).statements[0]
        assert isinstance(stmt.creation_datetime, datetime)

    def test_statement_creation_datetime_absent(self, camt053_balances_xml: str) -> None:
        stmt = parse_camt053(camt053_balances_xml).statements[0]
        assert stmt.creation_datetime is None

    def test_from_to_period_parsed(self, camt053_single_xml: str) -> None:
        stmt = parse_camt053(camt053_single_xml).statements[0]
        assert isinstance(stmt.from_datetime, datetime)
        assert isinstance(stmt.to_datetime, datetime)
        assert stmt.from_datetime == datetime(2026, 5, 9, 0, 0, 0)

    def test_period_absent_when_not_in_xml(self, camt053_balances_xml: str) -> None:
        stmt = parse_camt053(camt053_balances_xml).statements[0]
        assert stmt.from_datetime is None
        assert stmt.to_datetime is None

    def test_account_iban_extracted(self, camt053_single_xml: str) -> None:
        stmt = parse_camt053(camt053_single_xml).statements[0]
        assert stmt.account_iban == "DE89370400440532013000"

    def test_account_currency_extracted(self, camt053_single_xml: str) -> None:
        stmt = parse_camt053(camt053_single_xml).statements[0]
        assert stmt.account_currency == "EUR"


class TestParseCamt053Balances:
    """Balance projection: type code, amount, credit/debit, date."""

    def test_single_balance_parsed(self, camt053_single_xml: str) -> None:
        stmt = parse_camt053(camt053_single_xml).statements[0]
        assert len(stmt.balances) == 1

    def test_balance_type_code(self, camt053_single_xml: str) -> None:
        bal = parse_camt053(camt053_single_xml).statements[0].balances[0]
        assert bal.type_code == "OPBD"

    def test_balance_amount_and_currency(self, camt053_single_xml: str) -> None:
        bal = parse_camt053(camt053_single_xml).statements[0].balances[0]
        assert bal.amount.currency == "EUR"
        assert bal.amount.value == Decimal("10000.00")

    def test_balance_credit_debit(self, camt053_single_xml: str) -> None:
        bal = parse_camt053(camt053_single_xml).statements[0].balances[0]
        assert bal.credit_debit == "CRDT"

    def test_balance_date_as_date_type(self, camt053_single_xml: str) -> None:
        bal = parse_camt053(camt053_single_xml).statements[0].balances[0]
        assert isinstance(bal.balance_date, date)
        assert bal.balance_date == date(2026, 5, 9)

    def test_multiple_balances_all_parsed(self, camt053_balances_xml: str) -> None:
        stmt = parse_camt053(camt053_balances_xml).statements[0]
        assert len(stmt.balances) == 3

    def test_multiple_balances_type_codes(self, camt053_balances_xml: str) -> None:
        stmt = parse_camt053(camt053_balances_xml).statements[0]
        codes = [b.type_code for b in stmt.balances]
        assert codes == ["OPBD", "CLBD", "ITBD"]

    def test_debit_balance_credit_debit(self, camt053_balances_xml: str) -> None:
        stmt = parse_camt053(camt053_balances_xml).statements[0]
        itbd = next(b for b in stmt.balances if b.type_code == "ITBD")
        assert itbd.credit_debit == "DBIT"

    def test_no_entries_when_omitted(self, camt053_balances_xml: str) -> None:
        stmt = parse_camt053(camt053_balances_xml).statements[0]
        assert stmt.entries == []


class TestParseCamt053Entries:
    """Entry projection: ref, amount, status, dates, bank-tx codes, details."""

    def test_single_entry_parsed(self, camt053_single_xml: str) -> None:
        stmt = parse_camt053(camt053_single_xml).statements[0]
        assert len(stmt.entries) == 1

    def test_entry_ref(self, camt053_single_xml: str) -> None:
        entry = parse_camt053(camt053_single_xml).statements[0].entries[0]
        assert entry.entry_ref == "NTRY-001"

    def test_entry_amount_and_currency(self, camt053_single_xml: str) -> None:
        entry = parse_camt053(camt053_single_xml).statements[0].entries[0]
        assert entry.amount.value == Decimal("1500.00")
        assert entry.amount.currency == "EUR"

    def test_entry_credit_debit(self, camt053_single_xml: str) -> None:
        entry = parse_camt053(camt053_single_xml).statements[0].entries[0]
        assert entry.credit_debit == "DBIT"

    def test_entry_status_code(self, camt053_single_xml: str) -> None:
        entry = parse_camt053(camt053_single_xml).statements[0].entries[0]
        assert entry.status == "BOOK"

    def test_entry_booking_date(self, camt053_single_xml: str) -> None:
        entry = parse_camt053(camt053_single_xml).statements[0].entries[0]
        assert isinstance(entry.booking_date, date)
        assert entry.booking_date == date(2026, 5, 9)

    def test_entry_value_date(self, camt053_single_xml: str) -> None:
        entry = parse_camt053(camt053_single_xml).statements[0].entries[0]
        assert entry.value_date == date(2026, 5, 9)

    def test_entry_bank_tx_codes(self, camt053_single_xml: str) -> None:
        entry = parse_camt053(camt053_single_xml).statements[0].entries[0]
        assert entry.bank_tx_domain == "PMNT"
        assert entry.bank_tx_family == "ICDT"
        assert entry.bank_tx_subfamily == "ESCT"

    def test_entry_details_present(self, camt053_single_xml: str) -> None:
        entry = parse_camt053(camt053_single_xml).statements[0].entries[0]
        assert len(entry.entry_details) == 1

    def test_tx_details_end_to_end_id(self, camt053_single_xml: str) -> None:
        entry = parse_camt053(camt053_single_xml).statements[0].entries[0]
        tx = entry.entry_details[0].transactions[0]
        assert tx.end_to_end_id == "E2E-REF-001"

    def test_tx_details_instruction_id(self, camt053_single_xml: str) -> None:
        entry = parse_camt053(camt053_single_xml).statements[0].entries[0]
        tx = entry.entry_details[0].transactions[0]
        assert tx.instruction_id == "INSTR-001"

    def test_tx_details_amount(self, camt053_single_xml: str) -> None:
        entry = parse_camt053(camt053_single_xml).statements[0].entries[0]
        tx = entry.entry_details[0].transactions[0]
        assert tx.amount is not None
        assert tx.amount.value == Decimal("1500.00")
        assert tx.amount.currency == "EUR"

    def test_tx_details_credit_debit(self, camt053_single_xml: str) -> None:
        entry = parse_camt053(camt053_single_xml).statements[0].entries[0]
        tx = entry.entry_details[0].transactions[0]
        assert tx.credit_debit == "DBIT"


class TestParseCamt053BatchedEntry:
    """Batched entry: one entry with a Btch block and multiple TxDtls."""

    def test_batched_entry_batch_message_id(self, camt053_batched_xml: str) -> None:
        entry = parse_camt053(camt053_batched_xml).statements[0].entries[0]
        dtls = entry.entry_details[0]
        assert dtls.batch_message_id == "PAIN001-SALARY-20260509"

    def test_batched_entry_two_transactions(self, camt053_batched_xml: str) -> None:
        entry = parse_camt053(camt053_batched_xml).statements[0].entries[0]
        assert len(entry.entry_details[0].transactions) == 2

    def test_batched_entry_tx_end_to_end_ids(self, camt053_batched_xml: str) -> None:
        entry = parse_camt053(camt053_batched_xml).statements[0].entries[0]
        e2e_ids = [tx.end_to_end_id for tx in entry.entry_details[0].transactions]
        assert e2e_ids == ["E2E-SAL-1", "E2E-SAL-2"]

    def test_batched_entry_tx_amounts(self, camt053_batched_xml: str) -> None:
        entry = parse_camt053(camt053_batched_xml).statements[0].entries[0]
        amounts = [tx.amount.value for tx in entry.entry_details[0].transactions if tx.amount]
        assert amounts == [Decimal("3500.00"), Decimal("4200.00")]


class TestParseCamt053McpWrapper:
    """MCP-layer error handling in mcp_server.parse_camt053."""

    def test_empty_string_returns_error(self) -> None:
        from pactus.mcp_server import parse_camt053 as mcp_parse_camt053

        result = mcp_parse_camt053("")
        assert isinstance(result, dict)
        assert result["error"] == "empty input"

    def test_whitespace_only_returns_error(self) -> None:
        from pactus.mcp_server import parse_camt053 as mcp_parse_camt053

        result = mcp_parse_camt053("   ")
        assert isinstance(result, dict)
        assert "empty input" in result["error"]

    def test_malformed_xml_returns_error(self) -> None:
        from pactus.mcp_server import parse_camt053 as mcp_parse_camt053

        result = mcp_parse_camt053("<not valid xml")
        assert isinstance(result, dict)
        assert "error" in result

    def test_doctype_raises_unsafe_xml_error(self, camt053_single_xml: str) -> None:
        doctype_xml = '<?xml version="1.0"?><!DOCTYPE foo><root/>'
        with pytest.raises(UnsafeXmlError):
            parse_camt053(doctype_xml)

    def test_valid_xml_returns_parsed_camt053(self, camt053_single_xml: str) -> None:
        from pactus.core.domain.camt053 import ParsedCamt053

        result = parse_camt053(camt053_single_xml)
        assert isinstance(result, ParsedCamt053)
