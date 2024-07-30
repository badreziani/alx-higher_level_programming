#!/usr/bin/node

const request = require('request');
const fs = require('node:fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(filePath, response.body, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
