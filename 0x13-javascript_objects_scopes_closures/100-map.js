#!/usr/bin/node
/* eslint-disable */

let list = require("./100-data.js").list;
let list2 = list.map((x,i) => x*i);
console.log(list);
console.log(list2);
