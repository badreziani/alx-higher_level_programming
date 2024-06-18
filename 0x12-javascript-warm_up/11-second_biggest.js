#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const nums = process.argv.slice(2, process.argv.length).map(n => parseInt(n)).sort((n1, n2) => n1 - n2);
  console.log(nums[process.argv.length - 4]);
}
