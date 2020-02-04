#!/usr/bin/node

function factorial (x) {
  return x <= 2 ? x : x * factorial(x - 1);
}

console.log(factorial(+process.argv[2] || 1));
