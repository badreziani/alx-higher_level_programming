#!/usr/bin/node

const dict = require('./101-data.js').dict;

const result = Object.keys(dict).reduce((newDict, currentKey) => {
  if (newDict[dict[currentKey]] === undefined) {
    newDict[dict[currentKey]] = [];
  }
  newDict[dict[currentKey]].push(currentKey);
  return newDict;
}, {});

console.log(result);
