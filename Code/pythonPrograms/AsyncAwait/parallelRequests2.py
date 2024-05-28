import time
import asyncio


async def dosomething(i):
    print(f"The {i}th start")
    await asyncio.sleep(2)
    print(f"The {i}th end")


async def main():
    start = time.time()
    tasks = [dosomething(i+1) for i in range(10)]

    await asyncio.gather(*tasks)

    print(f"time: {time.time() - start} (s)")

if __name__ == "__main__":
    asyncio.run(main())