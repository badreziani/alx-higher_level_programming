#!/usr/bin/node
/** class Rectangle **/

module.exports = class Square extends require('./4-rectangle.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let x = 1; x <= this.size; x++) {
        let line = '';
        for (let y = 1; y <= this.size; y++) {
          line += c;
        }
        console.log(line);
      }
    }
  }
};
