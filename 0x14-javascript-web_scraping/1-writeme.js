#!/usr/bin/node

const fs = require('node:fs');
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, err => {
  if (err) {
    console.log(err);
  }
});
