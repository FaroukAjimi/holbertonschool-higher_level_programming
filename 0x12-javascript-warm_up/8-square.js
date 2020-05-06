#!/usr/bin/node
const process = require('process');
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
