import asyncio
from bleak import BleakClient

address = "78:02:B7:5A:09:06"
MODEL_NBR_UUID = "0906"

async def run(address, loop):
    async with BleakClient(address, loop=loop) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, loop))