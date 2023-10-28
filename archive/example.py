import asyncio
from asgiref.sync import async_to_sync


@async_to_sync
async def generate_text(input_text):
    # 模型生成文本的异步操作
    await asyncio.sleep(20)  # 模拟异步操作
    generated_text = "Generated text based on input: " + input_text
    return generated_text
