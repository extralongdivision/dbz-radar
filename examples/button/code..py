# SPDX-FileCopyrightText: 2020 FoamyGuy for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
This example script shows how to read button state with
debouncing that does not rely on time.sleep().
"""

import microcontroller
from digitalio import DigitalInOut, Direction, Pull

btn = DigitalInOut(microcontroller.pin.GPIO4)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

while True:
    current_state = btn.value
    if btn.value is False:  # active low
        print("Button pressed!")
    else:
        print("Waiting for user...")

