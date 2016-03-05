#!/usr/bin/env python

import max7219.led as led
import time
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

device = led.matrix(cascaded=1)
device.orientation(180)

device.show_message("MAX7219 LED Matrix Demo", font=proportional(CP437_FONT))

time.sleep(1)
device.letter(0, 3) #success
time.sleep(1)
device.scroll_right()
time.sleep(1)
device.letter(0, 3) #success
time.sleep(1)
device.scroll_right()
time.sleep(1)
device.letter(0, 3) #success
time.sleep(2)
device.letter(0, 1) #fail
time.sleep(2)
device.letter(0, 2) # alt fail