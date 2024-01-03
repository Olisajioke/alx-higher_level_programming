#!/usr/bin/node
// Script to get the contents of a webpage and store it in a file
const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.log('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  } else {
    console.error(error || `Failed to get content. Status code: ${response.statusCode}`);
  }
});
