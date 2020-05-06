#!/usr/bin/node
const process = require('process');
const array = 'C is fun';
for (let i = 1; i <= process.argv[2]; i++) {
  console.log(array);
}
