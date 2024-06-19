#!/usr/bin/node
/** class Rectangle **/

const Rectangle = require('./4-rectangle.js').Rectangle;

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
