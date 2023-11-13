0-javascript_is_amazing.js
#!/usr/bin/node
function add (a, b) {
  const c = a + b;
  console.log(c);
}

add(Number(process.argv[2]), Number(process.argv[3]));
