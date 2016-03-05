var Newman = require('newman');
var JSON5 = require('json5');
const fs = require('fs');


// read the collectionjson file 
var collectionJson = JSON5.parse(fs.readFileSync("TheBanksAPI.json.postman_collection", 'utf8'));
 
// define Newman options 
var newmanOptions = {
	envJson: JSON5.parse(fs.readFileSync("TB-VAT.postman_environment", "utf-8")), // environment file (in parsed json format) 
	outputFile: "outfile.json",            // the file to export to 
	asLibrary: true,         				// this makes sure the exit code is returned as an argument to the callback function 
	stopOnError: false
}
 
 var newmanCallback = function(data) {
     console.log(data);
 }
 
// Optional Callback function which will be executed once Newman is done executing all its tasks. 
Newman.execute(collectionJson, newmanOptions, newmanCallback);