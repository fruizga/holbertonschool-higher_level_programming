#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const a = this.width;
    const b = this.height;
    this.height = a;
    this.width = b;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
