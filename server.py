import xml.etree.ElementTree as ET
from fastmcp import FastMCP

mcp = FastMCP("iso20022-mcp")

@mcp.tool()
def hello(name: str) -> str:
  """Say hello to someone."""
  return f"Hello {name} from Pactus MCP server!"

@mcp.tool()
def parse_pacs008(xml: str) -> dict:
  """Parse a pacs.008 ISO 20022 payment message and extract key fields."""
  root = ET.fromstring(xml)
  ns = {"iso": "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08"}

  return {
    "message_id": root.find(".//iso:MsgId", ns).text,
    "amount": root.find(".//iso:IntrBkSttlmAmt", ns).text,
    "currency": root.find(".//iso:IntrBkSttlmAmt", ns).attrib["Ccy"],
    "debtor": root.find(".//iso:Dbtr/iso:Nm", ns).text,
    "debtor_bic": root.find(".//iso:DbtrAgt//iso:BICFI", ns).text,
    "creditor": root.find(".//iso:Cdtr/iso:Nm", ns).text,
    "creditor_bic": root.find(".//iso:CdtrAgt//iso:BICFI", ns).text,
  }

if __name__ == "__main__":
  mcp.run()