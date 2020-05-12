#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const file1 = fs.readFileSync(process.argv[2], (err) => { if (err) throw err; });
const file2 = fs.readFileSync(process.argv[3], (err) => { if (err) throw err; });
fs.writeFile(process.argv[4], file1 + file2, (err) => { if (err) throw err; });
