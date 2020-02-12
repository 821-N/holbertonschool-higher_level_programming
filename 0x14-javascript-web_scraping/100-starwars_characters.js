#!/usr/bin/node
/* eslint-disable */

const Request = require('request');

Request("http://swapi.co/api/films/"+process.argv[2], (error, response, body) => {
	let data = JSON.parse(body);
	data.characters.forEach(x => {
		Request(x, (error, response, body) => {
			let data = JSON.parse(body);
			console.log(data.name);
		});
	});
});
