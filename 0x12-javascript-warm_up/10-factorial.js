#!/usr/bin/node
const process = require('process');
function factorial (x) {
  if (x === 0) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}
console.log(factorial(parseInt(process.argv[2], 10) || 0));
