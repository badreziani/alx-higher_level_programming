#!/usr/bin/node

const OldSquare = require('./5-square.js');

module.exports = class Square extends OldSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let x = 1; x <= this.height; x++) {
        let line = '';
        for (let y = 1; y <= this.width; y++) {
          line += c;
        }
        console.log(line);
      }
    }
  }
};
