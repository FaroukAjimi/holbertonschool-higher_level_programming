#!/usr/bin/node
const process = require('process');
const fs = require('fs');
fs.writeFile(process.argv[4], `${process.argv[2]}\n${process.argv[3]}\n`, (err) => { if (err) throw err; });
