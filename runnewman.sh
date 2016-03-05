#!/bin/bash

collection=TheBanksAPI.json.postman_collection
env=TB-VAT.postman_environment
outfile=test-output.json

cd /home/pi/newt

touch test.lock
/usr/local/bin/newman --collection $collection --environment $env --outputFile $outfile > out.log
rm test.lock
