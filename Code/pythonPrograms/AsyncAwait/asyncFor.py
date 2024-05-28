import asyncio


class AsyncCounter(object):

    def __init__(self, stop=None):
        self.count = 0
        self.stop = stop

    def __aiter__(self):
        return self

    async def __anext__(self):
        await asyncio.sleep(1)
        self.count += 1
        if self.stop == self.count:
            raise StopAsyncIteration
        return self.count


async def main():
    async for i in AsyncCounter(11):
        print(i)


asyncio.run(main())