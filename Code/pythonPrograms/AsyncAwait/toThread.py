import asyncio
import threading

from time import sleep


def hard_work():
    print('thread id:', threading.get_ident())
    sleep(5)


async def do_async_job():
    # convert sync method to async.
    await asyncio.to_thread(hard_work)
    await asyncio.sleep(1)
    print('job done!')


async def main():
    task1 = asyncio.create_task(do_async_job())
    task2 = asyncio.create_task(do_async_job())
    task3 = asyncio.create_task(do_async_job())
    await asyncio.gather(task1, task2, task3)


asyncio.run(main())