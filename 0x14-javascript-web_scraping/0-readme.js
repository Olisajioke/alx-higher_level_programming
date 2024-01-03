#!/usr/bin/node
// Check if the correct number of arguments are provided

const fs = require('fs');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-readme.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
