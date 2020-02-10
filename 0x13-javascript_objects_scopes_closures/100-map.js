#!/usr/bin/node
/* eslint-disable */

let list = require("./100-data.js").list;
console.log(list);
console.log(list.map((x,i) => x*i));
