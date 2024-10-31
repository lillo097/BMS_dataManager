import asyncio
from bleak import BleakClient

device_address = "1273ABE0-DB65-668D-F268-797B1656C10B"

async def interact_with_device():
    async with BleakClient(device_address) as client:
        if client.is_connected:
            print(f"Connected to {device_address}")

            # Leggere il nome del produttore
            manufacturer_name_uuid = "00002a29-0000-1000-8000-00805f9b34fb"
            manufacturer_name = await client.read_gatt_char(manufacturer_name_uuid)
            print("Manufacturer:", manufacturer_name.decode())

            # Leggere il livello della batteria
            battery_level_uuid = "00002a19-0000-1000-8000-00805f9b34fb"
            battery_level = await client.read_gatt_char(battery_level_uuid)
            print("Battery Level:", int(battery_level[0]), "%")

# Esegui il loop asincrono
asyncio.run(interact_with_device())
