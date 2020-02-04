#!/usr/bin/node

const array = process.argv.slice(2);
array.sort((a, b) => b - a);
console.log(array[1] || 0);
