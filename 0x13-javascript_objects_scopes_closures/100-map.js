#!/usr/bin/node

const list = require('./100-data.js').list;

const newList = list.map((idx, el) => idx * el);

console.log(list);
console.log(newList);
