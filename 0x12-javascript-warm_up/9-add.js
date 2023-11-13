#!/usr/bin/node
function add(a, b) {
  const result = parseInt(a) + parseInt(b);
  console.log(result);
}

add(process.argv[2], process.argv[3]);
