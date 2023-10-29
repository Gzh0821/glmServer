import asyncio

from asgiref.sync import async_to_sync


@async_to_sync
async def generate_text(input_text: str) -> str:
    await asyncio.sleep(4)
    generated_text = "Generated text based on input: " + input_text
    return generated_text


@async_to_sync
async def generate_picture(prompt: str) -> str:
    await asyncio.sleep(8)
    return prompt
