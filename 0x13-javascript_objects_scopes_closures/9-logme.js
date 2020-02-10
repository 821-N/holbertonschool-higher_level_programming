#!/usr/bin/node
/* eslint-disable */

let count = 0;
exports.logMe = function(item) {
	console.log(count+": "+item);
	count++;
};
