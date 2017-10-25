import asyncio

async def hello_world():
    while True:
        print("hello world")
        await asyncio.sleep(1.5)

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
loop.close()