from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1024,
  messages=[
    {"role": "user", "content": "Say one sentence about what you are."}
  ]
)

print(message.content[0].text)