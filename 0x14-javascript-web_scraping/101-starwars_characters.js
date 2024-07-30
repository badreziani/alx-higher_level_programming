#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  const getCharacter = (index) => {
    if (index >= characters.length) {
      return;
    }
    request(characters[index], (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(JSON.parse(body).name);
      getCharacter(index + 1);
    });
  };
  getCharacter(0);
});
