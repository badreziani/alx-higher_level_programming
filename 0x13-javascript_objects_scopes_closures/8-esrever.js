#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduceRight((accumulator, currentElement) => {
    return accumulator.push(currentElement);
  }, []);
};
