#!/usr/bin/node
/* eslint-disable */

const Fs = require('fs');

Fs.readFile(process.argv[2], 'utf-8', (err, contents) => {
	if (err)
		console.log(err);
	else
		console.log(contents);
});
