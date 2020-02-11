#!/usr/bin/node
/* eslint-disable */

const Fs = require('fs');

Fs.writeFile(process.argv[2], process.argv[3], (err) => {
	if (err)
		console.log(err);
});
