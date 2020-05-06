#!/usr/bin/node
const process = require('process');
const array = 'C is fun';
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= parseInt(process.argv[2]); i++) {
    console.log(array);
  }
}
