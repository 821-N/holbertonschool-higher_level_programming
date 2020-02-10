#!/usr/bin/node
/* eslint-disable */

function checkWidth(w) {
	return Math.abs(parseInt(w)) === w;
}

class Rectangle {
	constructor(w, h) {
		if (!(checkWidth(w) && checkWidth(h)))
			return;
		this.width = w;
		this.height = h;
	}

	print() {
		for (let i=0; i<this.height; i++)
			console.log("X".repeat(this.width));
	}

	rotate() {
		[this.width, this.height] = [this.height, this.width];
	}

	double() {
		this.width *= 2;
		this.height *= 2;
	}
}

module.exports = Rectangle;
