import asyncio


async def greeting(name, delay):
    await asyncio.sleep(delay)
    print(f"hello {name}")


async def main():
    task1 = asyncio.create_task(greeting("Pety", 2))
    task2 = asyncio.create_task(greeting("Vasya", 1))

    await task1
    await task2


asyncio.run(main())


# todo: создать 100000 тасок create_task
