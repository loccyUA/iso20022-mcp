"""FastMCP server for Pactus — ISO 20022 payment message processing.

This module is the thin MCP wrapper. All business logic lives in
pactus.core. Tools registered here delegate to core parsers, validators,
converters, and the knowledge base.
"""

from fastmcp import FastMCP

mcp = FastMCP("pactus")


@mcp.tool
def ping() -> dict[str, str]:
    """Health check tool. Returns a static OK response.

    Real ISO 20022 tools will be added in subsequent migration steps.
    """
    return {"status": "ok", "service": "pactus-mcp", "version": "0.2.0"}


def main() -> None:
    """Entry point for the pactus-mcp console script."""
    mcp.run()


if __name__ == "__main__":
    main()
