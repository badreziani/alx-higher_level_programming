#!/usr/bin/node
/** class Rectangle **/

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let x = 1; x <= this.size; x++) {
        let line = '';
        for (let y = 1; y <= this.size; y++) {
          line += c;
        }
        console.log(line);
      }
    } else {
      this.print();
    }
  }
};
