#!/usr/bin/node
const Sqr = require('./5-square');

module.exports = class Square extends Sqr {
  charPrint (c) {
    let i = 0;
    if (c === undefined) {
      c = 'X';
    }
    for (i; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
};
