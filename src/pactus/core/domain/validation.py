"""Validation result models returned by the validate_* MCP tools."""

from __future__ import annotations

from pydantic import BaseModel


class ValidationViolation(BaseModel):
    line: int | None
    column: int | None
    path: str | None
    message: str
    domain: str
    type_name: str
    level: str


class ValidationReport(BaseModel):
    valid: bool
    schema_id: str
    violations: list[ValidationViolation]
