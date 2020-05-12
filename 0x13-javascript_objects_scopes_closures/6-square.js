#!/usr/bin/node
const square = require('./5-square');
module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  // method
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
};
