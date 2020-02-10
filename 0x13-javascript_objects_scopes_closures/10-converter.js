#!/usr/bin/node
/* eslint-disable */

exports.converter = function(base) {
	return (number) => number.toString(base);
}
