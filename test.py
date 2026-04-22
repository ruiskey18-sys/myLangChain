from llm_client import *




response = openai_client.responses.create(
    model="gpt-4.1-mini",
    input="你好，介绍一下你自己"
)

print(response.output_text)