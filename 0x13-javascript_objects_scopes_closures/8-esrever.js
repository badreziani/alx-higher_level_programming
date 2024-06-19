#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduceRight((accumulator, currentElement) => {
    accumulator.push(currentElement);
    return accumulator;
  }, []);
};
