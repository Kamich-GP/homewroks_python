import asyncio
import time
async def Red():
    print("Красный")
async def Yellow():
    await asyncio.sleep(6)
    print("Желтый")
    await asyncio.sleep(13)
    print("Желтый")
async def Green():
    await asyncio.sleep(8)
    print("Зеленый")
async def traficlight():
    red = asyncio.create_task(Red())
    yellow = asyncio.create_task(Yellow())
    green = asyncio.create_task(Green())
    await red
    await yellow
    await green
while True:
    time.sleep(2)
    asyncio.run(traficlight())