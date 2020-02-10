#!/usr/bin/node
/* eslint-disable */

let dict = require("./101-data.js").dict;
let out = {};
for (let x in dict) {
	let count = dict[x];
	if (out[count])
		out[count].push(x);
	else
		out[count] = [x];
}

console.log(out);
