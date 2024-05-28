import aiohttp
import asyncio
import time


def do_requests(session):
    return session.get('https://example.com')


async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(0, 10):
            tasks.append(do_requests(session))

        results = await asyncio.gather(*tasks)
        for r in results:
            print('example.com =>', r.status)
    print(f"time: {time.time() - start} (s)")


if __name__ == '__main__':
    asyncio.run(main())
