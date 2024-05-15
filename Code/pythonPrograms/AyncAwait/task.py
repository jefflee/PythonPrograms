import asyncio


async def coro():
    print('hello')
    await asyncio.sleep(1)
    print('world')


loop = asyncio.get_event_loop()
task = loop.create_task(coro())
loop.run_until_complete(task)