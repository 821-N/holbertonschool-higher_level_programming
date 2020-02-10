#!/usr/bin/node
/* eslint-disable */

exports.esrever = function(list) {
	let out = [];
	list.forEach(x => out.unshift(x));
	return out;
};
