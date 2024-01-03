#!/usr/bin/node
// Number of films with the given character ID
const request = require('request');
let filmCount = 0;

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes(18)) {
          filmCount += 1;
        }
      });
    });
    console.log(filmCount);
  }
});
