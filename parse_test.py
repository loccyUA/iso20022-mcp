import xml.etree.ElementTree as ET

tree = ET.parse("test_pacs008.xml")
root = tree.getroot()

ns = {"iso": "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08"}

msg_id = root.find(".//iso:MsgId", ns).text
amount = root.find(".//iso:IntrBkSttlmAmt", ns).text
currency = root.find(".//iso:IntrBkSttlmAmt", ns).attrib["Ccy"]
debtor = root.find(".//iso:Dbtr/iso:Nm", ns).text
creditor = root.find(".//iso:Cdtr/iso:Nm", ns).text
debtor_bic = root.find(".//iso:DbtrAgt//iso:BICFI", ns).text
creditor_bic = root.find(".//iso:CdtrAgt//iso:BICFI", ns).text

print(f"Message ID: {msg_id}")
print(f"Amount: {amount} {currency}")
print(f"Debtor: {debtor} ({debtor_bic})")
print(f"Creditor: {creditor} ({creditor_bic})")