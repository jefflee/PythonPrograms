import asyncio


async def do_async_job():
    await asyncio.sleep(2)
    print('never print')


async def main():
    try:
        await asyncio.wait_for(do_async_job(), timeout=1)
    except asyncio.TimeoutError:
        print('timeout!')


asyncio.run(main())