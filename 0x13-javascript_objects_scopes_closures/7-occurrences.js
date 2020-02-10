#!/usr/bin/node
/* eslint-disable */

module.exports.nbOccurences = function(list, searchElement) {
	return list.reduce((count,item) => count+(item === searchElement), 0);
};
