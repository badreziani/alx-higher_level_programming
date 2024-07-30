#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    JSON.parse(response.body).characters.map(charLink => {
      return request(charLink, (err, response, body) => {
        if (err) {
          return;
        }
        console.log(JSON.parse(response.body).name);
      });
    });
  }
});
