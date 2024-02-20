import asyncio


async def greeting(name, delay):
    await asyncio.sleep(delay)
    print(f"hello {name}")


async def main():
    await greeting("Pety", 2)
    await greeting("Vasya", 1)


asyncio.run(main())
