#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const nums = process.argv.slice(2, process.argv.length).map(arg => parseInt(arg)).sort();
  console.log(nums[process.argv.length - 4]);
}
