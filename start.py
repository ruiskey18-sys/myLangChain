from llm_client import *
# from agents import Agent, Runner
import asyncio



# 文字调用api
# response = openai_client.responses.create(
#     model="gpt-4.1-mini",
#     input="你好，介绍一下你自己"
# )
# print(response.output_text)

# 图片资源调用api
# response = openai_client.responses.create(
#     model="gpt-5",
#     input=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_text",
#                     "text": "What teams are playing in this image?",
#                 },
#                 {
#                     "type": "input_image",
#                     "image_url": "https://api.nga.gov/iiif/a2e6da57-3cd1-4235-b20e-95dcaefed6c8/full/!800,800/0/default.jpg"
#                 }
#             ]
#         }
#     ]
# )
#
# print(response.output_text)


# extend the model with tools
# response = openai_client.responses.create(
#     model="gpt-5.4",
#     tools=[{"type": "web_search"}],
#     input="What was a positive news story from today?"
# )
#
# print(response.output_text)


stream = openai_client.responses.create(
    model="gpt-5",
    input=[
        {
            "role": "user",
            "content": "Say 'double bubble bath' ten times fast.",
        },
    ],
    stream=True,
)

for event in stream:
    print(event)



# build agents
# spanish_agent = Agent(
#     name="Spanish agent",
#     instructions="You only speak Spanish.",
# )
#
# english_agent = Agent(
#     name="English agent",
#     instructions="You only speak English",
# )
#
# triage_agent = Agent(
#     name="Triage agent",
#     instructions="Handoff to the appropriate agent based on the language of the request.",
#     handoffs=[spanish_agent, english_agent],
# )
#
#
# async def main():
#     result = await Runner.run(triage_agent, input="Hola, ¿cómo estás?")
#     print(result.final_output)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())