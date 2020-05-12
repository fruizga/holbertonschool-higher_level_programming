#!/usr/bin/node

const Sqr_ = require('./5-square');
module.exports = class Square extends Sqr_ {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
