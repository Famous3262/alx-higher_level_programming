#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';
let movienum = 0;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const movies = JSON.parse(body);
    movies.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          movienum += 1;
        }
      });
    });
    console.log(movienum);
  }
});
