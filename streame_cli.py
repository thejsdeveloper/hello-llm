import asyncio
import os
import time
from openai import AsyncOpenAI
from openai.types.responses import Response

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPEN_ROUTER_KEY"]
)

QUESTION = "Explain SSE in 3 sentences"


async def ask(model: str, label: str) -> float:
    print(f"----------{label}--------------")
    start = time.perf_counter()

    async with client.responses.stream(
        model=model, input=[{"role": "user", "content": QUESTION}]
    ) as stream:
        async for event in stream:
            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)

        final_response: Response = await stream.get_final_response()
        print(f"\n[{final_response.usage.output_tokens} output tokens]")

    return time.perf_counter() - start


async def run():
    haiku_time = await ask("anthropic/claude-haiku-4.5", "HAIKU")
    sonnet_time = await ask("anthropic/claude-sonnet-4.5", "SONNET")
    sequential_total = haiku_time + sonnet_time

    start = time.perf_counter()
    await asyncio.gather(
        ask("anthropic/claude-haiku-4.5", "HAIKU (concurrent)"),
        ask("anthropic/claude-sonnet-4.5", "SONNET (concurrent)"),
    )
    concurrent_total = time.perf_counter() - start

    print("---------TIMING----------")
    print(f"sequential (one after another): {sequential_total:.2f}s")
    print(f"concurrent (asyncio.gather):    {concurrent_total:.2f}s")


asyncio.run(run())
