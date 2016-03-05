#!/usr/bin/python

import json
import os
import sys
import time
import max7219.led as led
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

# test if .lock file exists and if yes, exit
if os.path.isfile('test.lock'):
    print ('found lock file, will exit')
    sys.exit()
else:
    print ('file test.lock does not exist')

# and if we have results at all
if os.path.isfile('test-output.json'):
    print ('found test-output.json, will process')
else:
    print ('file test-output.json does not exist, will exit')
    sys.exit()

# no running test, setup the rest
device = led.matrix(cascaded=1)
device.orientation(180)

#device.show_message("MAX7219", font=proportional(CP437_FONT))

runFailed = False

# check last test run
with open('test-output.json') as data_file:    
    data = json.load(data_file)

for result in data['results']:
    runFailed = runFailed or (result['totalPassFailCounts']['fail'] > 0)
    
# very simple logic for showing that script is alive
tickFlag = 'l'
if os.path.isfile('tick-flag.txt'):
    with open('tick-flag.txt', 'r') as tickFlagFile:
        tickFlag=tickFlagFile.read()

if (tickFlag =='l'):
    tickFlag = 'r'
else:
    tickFlag = 'l'

with open('tick-flag.txt', 'w') as tickFlagFile:
    tickFlagFile.write(tickFlag)
    
# draw status icon
if (runFailed):
    if (tickFlag=='l'):
        device.letter(0, 1)
    else:
        device.letter(0, 2)
else:
    device.letter(0, 3)
    if (tickFlag=='r'):
        device.scroll_right()
    
print ('done')