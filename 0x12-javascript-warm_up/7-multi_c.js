#!/usr/bin/node
const numOccurrences = process.argv[2];
if (numOccurrences === undefined || isNaN(numOccurrences)) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(numOccurrences);
  let i = 0;

  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
