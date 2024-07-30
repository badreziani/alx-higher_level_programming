#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '/18/';

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(response.body).results.filter(film => {
      return film.characters.find(link => link.endsWith(characterId));
    }).length);
  }
});
