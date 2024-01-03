#!/usr/bin/node
// script that prints starwars movie characters
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(`Characters in ${movieData.title}:`);
    movieData.characters.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (!charError && charResponse.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        } else {
          console.error(charError || 'Failed to fetch character details');
        }
      });
    });
  } else {
    console.error(error || 'Failed to fetch movie details');
  }
});
