var JSON5 = require('json5'),
    winston = require('winston');

const fs = require('fs');
var process = require ('process');

//newman --collection TheBanksAPI.json.postman_collection --environment TB-VAT.postman_environment --number 1

var log = new (winston.Logger)(
    {
        exitOnError: false,
        transports: [
            new (winston.transports.Console)({ level: 'debug', colorize: 'true', 'timestamp': true }) //,
			//new (winston.transports.File)({ filename: nconf.get('app:log'), level: 'info', 'timestamp': true })
		]
    }
);

log.info ('test if we have lock file from test in progress')
var lockFileExists = false;
try {
    fs.accessSync('test.lock');
    lockFileExists  = true;  
}
catch (ex) {
    //do nothing, as accessSync throws if there is no file and that's fine
}

if (lockFileExists) {
    log.info ('found lock file, will exit')
    process.exit(0)
}
else {
    log.info('could not find test lock file, will continue execution');
}

var r = JSON5.parse(fs.readFileSync('o.json', 'utf8'));

var failedTests = r.results.filter(function (res) {
    return res.totalPassFailCounts.fail > 0;
});

if (failedTests.length > 0) {
    log.info ('there are failed tests');
}
else {
    log.info ('no failed tests');
}