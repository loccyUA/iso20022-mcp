"""XSD-backed validators for ISO 20022 messages.

Each validator returns a ValidationReport listing every violation found
rather than stopping at the first error. XSDs are loaded once at import
time via importlib.resources so they work both in editable installs and
installed wheels.
"""

from __future__ import annotations

from importlib.resources import files as _res_files

import lxml.etree as _etree

from pactus.core.domain.validation import ValidationReport, ValidationViolation
from pactus.core.parsers import UnsafeXmlError as _UnsafeXmlError  # re-export
from pactus.core.parsers import _lxml_parser, _reject_unsafe_xml

UnsafeXmlError = _UnsafeXmlError

_SCHEMAS_PKG = _res_files("pactus").joinpath("schemas")


def _load_schema(xsd_filename: str) -> _etree.XMLSchema:
    ref = _SCHEMAS_PKG.joinpath(xsd_filename)
    with ref.open("rb") as f:
        return _etree.XMLSchema(_etree.parse(f))


_PACS008_SCHEMA: _etree.XMLSchema = _load_schema("pacs.008.001.08.xsd")
_PACS002_SCHEMA: _etree.XMLSchema = _load_schema("pacs.002.001.10.xsd")
_PAIN001_SCHEMA: _etree.XMLSchema = _load_schema("pain.001.001.09.xsd")
_CAMT053_SCHEMA: _etree.XMLSchema = _load_schema("camt.053.001.08.xsd")


def _validate(xml: str, schema: _etree.XMLSchema, schema_id: str) -> ValidationReport:
    _reject_unsafe_xml(xml)
    try:
        doc = _etree.fromstring(xml.encode("utf-8"), _lxml_parser)
    except _etree.XMLSyntaxError as exc:
        return ValidationReport(
            valid=False,
            schema_id=schema_id,
            violations=[
                ValidationViolation(
                    line=exc.lineno or None,
                    column=exc.offset or None,
                    path=None,
                    message=exc.msg or str(exc),
                    domain="PARSER",
                    type_name="XMLSyntaxError",
                    level="FATAL",
                )
            ],
        )

    schema.validate(doc)
    violations = [
        ValidationViolation(
            line=err.line or None,
            column=err.column or None,
            path=err.path if err.path else None,
            message=err.message,
            domain=err.domain_name,
            type_name=err.type_name,
            level=err.level_name,
        )
        for err in schema.error_log
    ]
    return ValidationReport(
        valid=len(violations) == 0,
        schema_id=schema_id,
        violations=violations,
    )


def validate_pacs008(xml: str) -> ValidationReport:
    """Validate a pacs.008.001.08 message against its XSD."""
    return _validate(xml, _PACS008_SCHEMA, "pacs.008.001.08")


def validate_pacs002(xml: str) -> ValidationReport:
    """Validate a pacs.002.001.10 message against its XSD."""
    return _validate(xml, _PACS002_SCHEMA, "pacs.002.001.10")


def validate_pain001(xml: str) -> ValidationReport:
    """Validate a pain.001.001.09 message against its XSD."""
    return _validate(xml, _PAIN001_SCHEMA, "pain.001.001.09")


def validate_camt053(xml: str) -> ValidationReport:
    """Validate a camt.053.001.08 message against its XSD."""
    return _validate(xml, _CAMT053_SCHEMA, "camt.053.001.08")
