import asyncio
from bleak import BleakScanner
import time

SMOOTH_COUNT = 15
ID = ["H213", "H214", "H215", "H216", "H217"]

async def run():
    smooth_count = 0
    smooth_rssi = 0.0
    for i in range(5):
        while(True):
            rssi = await getRSSI(ID[i])

            if(rssi > -1):
                smooth_rssi += rssi
                smooth_count += 1

                if(smooth_count == SMOOTH_COUNT):
                    smooth_rssi /= smooth_count

                    print(f"Signal: {smooth_rssi}")

                    if checkRSSI():
                        print(f"REACHED ROOM {ID[i]}")
                        print(f"NOW LOOKING FOR ROOM {ID[i + 1]}")
                        smooth_rssi = 0
                        smooth_count = 0
                        break


                    smooth_rssi = 0
                    smooth_count = 0

async def checkRSSI(smooth_rssi):
    return smooth_rssi < 55 and smooth_rssi > 0

async def getRSSI(name):
    try:
        devices = await BleakScanner.discover(timeout=0.1)
    except:
        return -1
    
    for d in devices:
        if(d.name == name):
            return -d.rssi
    
    return -1

loop = asyncio.get_event_loop()
loop.run_until_complete(run())