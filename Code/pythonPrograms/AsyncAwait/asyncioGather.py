import asyncio
import threading
import random
from datetime import datetime


async def do_async_job():
    await asyncio.sleep(2)
    print(datetime.now().isoformat(), 'thread id', threading.current_thread().ident)
    return random.randint(1, 10)


async def main():
    job1 = do_async_job()
    job2 = do_async_job()
    job3 = do_async_job()
    return_values  = await asyncio.gather(job1, job2, job3)

    for v in return_values:
        print('result =>', v)


asyncio.run(main())