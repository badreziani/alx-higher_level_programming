#!/usr/bin/node

const factorial = function (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return parseInt(n) * factorial(parseInt(n) - 1);
};

console.log(factorial(process.argv[2]));
