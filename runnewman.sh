#!/bin/bash

collection=TheBanksAPI.json.postman_collection
env=TB-VAT.postman_environment
outfile=test-output.json

touch test.lock
newman --collection $collection --environment $env --outputFile $outfile > out.log
rm test.lock
