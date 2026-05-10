"""Curated domain models for ISO 20022 messages.

These are the LLM-facing Pydantic models returned by MCP tools. They are
hand-written projections of the xsdata-generated models in
pactus.generated.* — kept clean, flat, and free of XML-specific types.
"""

from pactus.core.domain.common import Agent, Amount, Party
from pactus.core.domain.pacs008 import (
    ChargeBearer,
    GroupHeader,
    Pacs008Transaction,
    ParsedPacs008,
    SettlementMethod,
)

__all__ = [
    "Agent",
    "Amount",
    "ChargeBearer",
    "GroupHeader",
    "Pacs008Transaction",
    "ParsedPacs008",
    "Party",
    "SettlementMethod",
]
