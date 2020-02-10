#!/usr/bin/node
/* eslint-disable */
function checkWidth(w) {
	return Math.sign(parseInt(w)) === 1;
}

class Rectangle {
	constructor(w, h) {
		if (!(checkWidth(w) && checkWidth(h)))
			return;
		this.width = w;
		this.height = h;
	}
}

module.exports = Rectangle;
