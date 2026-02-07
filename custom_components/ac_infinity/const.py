"""Constants for the ac_infinity integration."""
from bleak.exc import BleakError

DOMAIN = "ac_infinity"

DEVICE_TIMEOUT = 30
UPDATE_SECONDS = 15

BLEAK_EXCEPTIONS = (AttributeError, BleakError, TimeoutError)

DEVICE_MODEL = {
    1: "Controller 67",
    2: "Controller Type B",
    3: "Controller Type C",
    4: "Controller Type C",
    5: "Controller Type C",
    6: "Controller 69",
    7: "Controller 69",
    8: "Controller Type E",
    9: "Controller 69 Pro",
    11: "Controller 69 Pro",
    12: "Controller 69 Pro+",
    14: "Controller Type C",
    15: "Controller Type C",
}
