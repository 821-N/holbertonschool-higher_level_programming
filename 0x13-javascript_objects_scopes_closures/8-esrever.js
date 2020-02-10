#!/usr/bin/node
/* eslint-disable */

exports.esrever = function(list) {
	var out = [];
	list.forEach(x => out.unshift(x));
	return out;
};
