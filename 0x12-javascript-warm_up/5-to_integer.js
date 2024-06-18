#!/usr/bin/node
console.log((Number.isNaN(process.argv[2]) || !process.argv[2]) ? 'Not a number' : 'My number: ' + parseInt(process.argv[2]));
