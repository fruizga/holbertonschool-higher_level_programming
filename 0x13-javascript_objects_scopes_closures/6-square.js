#!/usr/bin/node
const Sqr = require('./5-square');

module.exports = class Square extends Sqr {
  charPrint (char) {
    let i = 0;
    if (char === undefined) {
      char = 'X';
    }
    for (i; i < this.size; i++) {
      console.log(char.repeat(this.size));
    }
  }
};
