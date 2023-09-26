#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;
  for (const character of characters) {
    request(character, (err, res, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const movieData = JSON.parse(body);
      console.log(movieData.name);
    });
  }
});
