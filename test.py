import json
import time

runFailed=1
#print(runFailed)

with open('test-output.json') as data_file:    
    data = json.load(data_file)

for result in data['results']:
    runFailed = runFailed or (result['totalPassFailCounts']['fail'] > 0)
    #print(result['totalPassFailCounts']['fail'] > 0)


print(runFailed)

tickFlag = 'l'
with open('tick-flag.txt', 'r') as tickFlagFile:
    tickFlag=tickFlagFile.read()

print(tickFlag)

if (tickFlag =='l'):
    tickFlag = 'r'
else:
    tickFlag = 'l'

print(tickFlag)

with open('tick-flag.txt', 'w') as tickFlagFile:
    tickFlagFile.write(tickFlag)

if (runFailed):
    if (tickFlag=='l'):
       print('fail l')
    else:
        print('fail r')
else:
    if (tickFlag=='l'):
        print('success l')
    else:
        print('success r')
