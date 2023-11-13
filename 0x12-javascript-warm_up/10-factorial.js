#!/usr/bin/node
function factorial(n) {
  if (isNaN(n)) {
    console.log(1);
  } else if (n === 0) {
    console.log(1);
  } else {
    const result = calculateFactorial(n);
    console.log(result);
  }
}

function calculateFactorial(num) {
  if (num === 1) {
    return 1;
  } else {
    return num * calculateFactorial(num - 1);
  }
}

const number = Number(process.argv[2]);
factorial(number);
