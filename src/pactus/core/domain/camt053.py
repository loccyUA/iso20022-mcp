"""Domain models for camt.053.001.08 — Bank-to-Customer Cash Management Statement.

The reporting message in a reconciliation flow: a bank sends its customer
a structured account statement covering a period. Structurally the deepest
hierarchy in this codebase: GroupHeader → Statement[] → Balance[] + Entry[]
→ EntryDetails[] → TransactionDetails[].

These are hand-curated LLM-facing models projected from xsdata-generated
classes in pactus.generated.camt_053_001_08. Generated classes never escape
the parser layer.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from pactus.core.domain.common import Amount

CreditDebit = Literal["CRDT", "DBIT"]


class GroupHeader(BaseModel):
    """Message-level metadata for the whole camt.053."""

    model_config = ConfigDict(extra="forbid")

    message_id: str = Field(description="MsgId of this statement report.")
    creation_datetime: datetime = Field(description="When this message was generated.")


class Balance(BaseModel):
    """One balance figure reported for an account."""

    model_config = ConfigDict(extra="forbid")

    type_code: str = Field(
        description="Balance type code (e.g. 'OPBD' opening booked, 'CLBD' closing booked). "
        "Taken from CdOrPrtry.Cd; falls back to CdOrPrtry.Prtry if no standard code.",
    )
    amount: Amount = Field(description="Balance amount and currency.")
    credit_debit: CreditDebit = Field(description="Whether the balance is a credit or debit.")
    balance_date: date = Field(description="Date to which the balance applies.")


class TransactionDetails(BaseModel):
    """References and amounts for one transaction within an entry batch."""

    model_config = ConfigDict(extra="forbid")

    end_to_end_id: str | None = Field(
        default=None,
        description="End-to-end identifier carried from the originating message.",
    )
    instruction_id: str | None = Field(
        default=None,
        description="Instruction identifier.",
    )
    transaction_id: str | None = Field(
        default=None,
        description="Transaction identifier assigned by the bank.",
    )
    amount: Amount | None = Field(
        default=None,
        description="Transaction amount, if reported at this level.",
    )
    credit_debit: CreditDebit | None = Field(
        default=None,
        description="Credit/debit indicator at the transaction level.",
    )


class EntryDetails(BaseModel):
    """Transaction details nested under one entry (may cover a batch)."""

    model_config = ConfigDict(extra="forbid")

    batch_message_id: str | None = Field(
        default=None,
        description="Batch/file identifier when this entry covers a batch payment.",
    )
    transactions: list[TransactionDetails] = Field(
        default_factory=list,
        description="Individual transaction references within this entry.",
    )


class Entry(BaseModel):
    """One debit or credit entry on the account statement."""

    model_config = ConfigDict(extra="forbid")

    entry_ref: str | None = Field(
        default=None,
        description="Bank's own reference for this entry.",
    )
    amount: Amount = Field(description="Entry amount and currency.")
    credit_debit: CreditDebit = Field(
        description="Whether this entry debits or credits the account."
    )
    status: str = Field(
        description="Entry status code (e.g. 'BOOK' booked, 'PDNG' pending, 'INFO' information).",
    )
    booking_date: date | None = Field(
        default=None,
        description="Date the entry was booked to the account.",
    )
    value_date: date | None = Field(
        default=None,
        description="Value date of the entry for interest calculation.",
    )
    bank_tx_domain: str | None = Field(
        default=None,
        description="ISO bank transaction domain code (e.g. 'PMNT' payments).",
    )
    bank_tx_family: str | None = Field(
        default=None,
        description="ISO bank transaction family code (e.g. 'ICDT' issued credit transfers).",
    )
    bank_tx_subfamily: str | None = Field(
        default=None,
        description="ISO bank transaction sub-family code (e.g. 'ESCT' SEPA credit transfer).",
    )
    entry_details: list[EntryDetails] = Field(
        default_factory=list,
        description="Detailed transaction info nested within this entry.",
    )


class Statement(BaseModel):
    """One account statement block within the camt.053 message."""

    model_config = ConfigDict(extra="forbid")

    statement_id: str = Field(description="Statement identifier assigned by the bank.")
    creation_datetime: datetime | None = Field(
        default=None,
        description="When this statement was generated.",
    )
    from_datetime: datetime | None = Field(
        default=None,
        description="Start of the reporting period.",
    )
    to_datetime: datetime | None = Field(
        default=None,
        description="End of the reporting period.",
    )
    account_iban: str | None = Field(
        default=None,
        description="Account IBAN.",
    )
    account_currency: str | None = Field(
        default=None,
        description="Account currency (ISO 4217).",
    )
    balances: list[Balance] = Field(
        description="Balance figures for the account (opening, closing, etc.).",
    )
    entries: list[Entry] = Field(
        default_factory=list,
        description="Debit and credit entries recorded on the statement.",
    )


class ParsedCamt053(BaseModel):
    """A fully-parsed camt.053.001.08 Bank-to-Customer Statement."""

    model_config = ConfigDict(extra="forbid")

    group_header: GroupHeader
    statements: list[Statement]
