#!/usr/bin/node
/** class Rectangle **/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 1; x <= this.height; x++) {
      let line = '';
      for (let y = 1; y <= this.width; y++) {
        line += 'X';
      }
      console.log(line);
    }
  }
};
