#!/usr/bin/node
/* eslint-disable */

const Request = require('request');

Request(process.argv[2], (error, response, body) => {
	let data = JSON.parse(body);
	let count = 0;
	data.results.forEach(item => {
		count += item.characters.some(item => /[^\d]18[^\d]/.test(item));
	});
	console.log(count);
});
