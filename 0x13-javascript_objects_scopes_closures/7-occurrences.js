#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((accumulator, currentElement) => currentElement === searchElement ? accumulator + 1 : accumulator, 0);
};
