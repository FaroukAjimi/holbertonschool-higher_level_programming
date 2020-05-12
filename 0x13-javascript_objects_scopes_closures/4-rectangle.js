#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) { return; }
    this.width = w;
    this.height = h;
  }

  // method
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // method
  rotate () {
    let aux = 0;
    aux = this.height;
    this.height = this.width;
    this.width = aux;
  }

  // method
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
