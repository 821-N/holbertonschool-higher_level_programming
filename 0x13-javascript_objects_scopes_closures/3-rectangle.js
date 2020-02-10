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

	print() {
		for (var i=0; i<this.height; i++)
			console.log("X".repeat(this.width));
	}
}

module.exports = Rectangle;
