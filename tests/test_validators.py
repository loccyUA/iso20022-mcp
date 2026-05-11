"""Unit tests for pactus.core.validators — exercises validation logic directly.

These tests cover the validator functions themselves (not the MCP wrapper).
MCP-layer concerns (empty input guard, exception wrapping, tool dispatch) are
covered in test_mcp_integration.py instead.
"""

from __future__ import annotations

import pytest

from pactus.core.parsers import UnsafeXmlError
from pactus.core.validators import (
    validate_camt053,
    validate_pacs002,
    validate_pacs008,
    validate_pain001,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_VALIDATE_FNS = {
    "pacs008": validate_pacs008,
    "pacs002": validate_pacs002,
    "pain001": validate_pain001,
    "camt053": validate_camt053,
}

_SCHEMA_IDS = {
    "pacs008": "pacs.008.001.08",
    "pacs002": "pacs.002.001.10",
    "pain001": "pain.001.001.09",
    "camt053": "camt.053.001.08",
}

# Minimal well-formed XML with the correct namespace but wrong structure —
# XSD validation will fail with at least one violation.
_INVALID_STRUCTURED: dict[str, str] = {
    "pacs008": (
        '<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08">'
        "<WrongElement/></Document>"
    ),
    "pacs002": (
        '<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.002.001.10">'
        "<WrongElement/></Document>"
    ),
    "pain001": (
        '<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pain.001.001.09">'
        "<WrongElement/></Document>"
    ),
    "camt053": (
        '<Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.053.001.08">'
        "<WrongElement/></Document>"
    ),
}

_DOCTYPE_XML = '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY x "y">]><root/>'
_MALFORMED_XML = "<unclosed"


# ---------------------------------------------------------------------------
# Valid documents return valid=True
# ---------------------------------------------------------------------------


class TestValidHappyPath:
    def test_pacs008_valid(self, pacs008_single_xml: str) -> None:
        report = validate_pacs008(pacs008_single_xml)
        assert report.valid is True
        assert report.violations == []
        assert report.schema_id == "pacs.008.001.08"

    def test_pacs002_valid(self, pacs002_single_xml: str) -> None:
        report = validate_pacs002(pacs002_single_xml)
        assert report.valid is True
        assert report.violations == []
        assert report.schema_id == "pacs.002.001.10"

    def test_pain001_valid(self, pain001_single_xml: str) -> None:
        report = validate_pain001(pain001_single_xml)
        assert report.valid is True
        assert report.violations == []
        assert report.schema_id == "pain.001.001.09"

    def test_camt053_valid(self, camt053_single_xml: str) -> None:
        report = validate_camt053(camt053_single_xml)
        assert report.valid is True
        assert report.violations == []
        assert report.schema_id == "camt.053.001.08"


# ---------------------------------------------------------------------------
# XSD violations are reported (not raised)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("key", list(_INVALID_STRUCTURED))
def test_invalid_structured_returns_violations(key: str) -> None:
    fn = _VALIDATE_FNS[key]
    report = fn(_INVALID_STRUCTURED[key])
    assert report.valid is False
    assert report.schema_id == _SCHEMA_IDS[key]
    assert len(report.violations) >= 1
    v = report.violations[0]
    assert v.message  # non-empty
    assert v.level in {"ERROR", "WARNING", "FATAL"}
    assert v.domain  # non-empty string from lxml


# ---------------------------------------------------------------------------
# Malformed XML → single FATAL violation, no raise
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("key", list(_VALIDATE_FNS))
def test_malformed_xml_returns_single_fatal(key: str) -> None:
    fn = _VALIDATE_FNS[key]
    report = fn(_MALFORMED_XML)
    assert report.valid is False
    assert len(report.violations) == 1
    v = report.violations[0]
    assert v.level == "FATAL"
    assert v.type_name == "XMLSyntaxError"
    assert v.domain == "PARSER"
    assert v.message  # non-empty


# ---------------------------------------------------------------------------
# Violation fields are populated
# ---------------------------------------------------------------------------


def test_violation_has_line_info(pacs008_single_xml: str) -> None:
    corrupted = pacs008_single_xml.replace("<NbOfTxs>1</NbOfTxs>", "")
    report = validate_pacs008(corrupted)
    assert report.valid is False
    assert len(report.violations) >= 1
    # At least one violation should carry a line number
    lines = [v.line for v in report.violations if v.line is not None]
    assert lines, "expected at least one violation with a line number"
    assert all(ln >= 1 for ln in lines)


# ---------------------------------------------------------------------------
# UnsafeXmlError propagates (not swallowed at this layer)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("key", list(_VALIDATE_FNS))
def test_doctype_raises_unsafe_xml_error(key: str) -> None:
    fn = _VALIDATE_FNS[key]
    with pytest.raises(UnsafeXmlError):
        fn(_DOCTYPE_XML)
