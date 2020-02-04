#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89;
Object.freeze(myObject); // w
console.log(myObject);
