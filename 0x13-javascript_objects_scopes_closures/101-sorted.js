#!/usr/bin/node

const dict = require('./101-data.js').dict;

const keys = Object.keys(dict);

const newDict = {};

keys.map(key => {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
});

console.log(newDict);
