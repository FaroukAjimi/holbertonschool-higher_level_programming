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
      console.log(c.repeat(this.size));
    }
  }
};
