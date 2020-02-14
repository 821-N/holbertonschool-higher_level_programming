#!/usr/bin/node
/* eslint-disable */

const Request = require('request');
const Fs = require('fs');

Request(process.argv[2], (error, response, body) => {
	let data = JSON.parse(body);
	let counts = {};
	data.forEach(task => {
		if (task.completed) {
			let id = task.userId;
			if (!counts[id])
				counts[id] = 1;
			else
				counts[id]++;
		}
	});
	console.log(counts);
});
