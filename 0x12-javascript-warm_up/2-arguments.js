#!/usr/bin/node

console.log([
  'No argument',
  'Argument found',
  'Arguments found'
][Math.min(process.argv.length - 2, 2)]);
