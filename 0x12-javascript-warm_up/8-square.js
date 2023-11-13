#!/usr/bin/node
const size = process.argv[2];
if (size === undefined || isNaN(size)) {
  console.log('Missing size');
} else {
  const x = Number(size);
  let i = 0;

  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
