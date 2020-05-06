#!/usr/bin/node
const process = require('process');
let largest = 0;
let l = 0;
for (let i = 2; parseInt(process.argv[i]); i++) {
  if (parseInt(process.argv[i]) > largest){
      largest=process.argv[i];
}}
console.log(largest)
