import asyncio
from bleak import BleakScanner, BleakClient


async def get_device_info(device):
    device_info = {
        "Name": device.name,
        "Address": device.address,
        "RSSI": device.rssi,
        "Details": device.details,
        "Metadata": device.metadata,
        "Services": []
    }

    try:
        async with BleakClient(device) as client:
            services = await client.get_services()
            for service in services:
                service_info = {
                    "UUID": service.uuid,
                    "Characteristics": []
                }
                for characteristic in service.characteristics:
                    characteristic_info = {
                        "UUID": characteristic.uuid,
                        "Properties": characteristic.properties,
                        "Descriptors": []
                    }
                    for descriptor in characteristic.descriptors:
                        characteristic_info["Descriptors"].append(descriptor.uuid)
                    service_info["Characteristics"].append(characteristic_info)
                device_info["Services"].append(service_info)
    except Exception as e:
        print(f"Could not connect to {device.name}: {e}")

    return device_info


async def run():
    print("Scanning for BLE devices...")
    devices = await BleakScanner.discover(timeout=10)  # Timeout di 10 secondi per la scansione

    if not devices:
        print("No BLE devices found.")
        return

    for device in devices:
        print(f"\nScanning device: {device.name} ({device.address})")
        device_info = await get_device_info(device)
        print(device_info)
        print("-" * 1000)


# Avvio del loop asincrono
if __name__ == "__main__":
    asyncio.run(run())
