import beacon_console

#Test case for if rssi is correct
#Hold the beacon approx 0.5m away from the device
async def test_get_rssi():
    rssi = beacon_console.getRSSI("H213")

    assert 40 < rssi < 50

async def test_check_rssi():
    rssi = beacon_console.checkRSSI(23)

    assert rssi

async def test_check_rssi_2():
    rssi = beacon_console.checkRSSI(1)

    assert rssi

async def test_check_rssi_3():
    rssi = beacon_console.checkRSSI(54)

    assert rssi