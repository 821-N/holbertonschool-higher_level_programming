#!/usr/bin/node
/* eslint-disable */

const Request = require('request');

Request("http://swapi.co/api/films/"+process.argv[2], (error, response, body) => {
	let data = JSON.parse(body);
	let list = [];
	let gotten = 0;
	data.characters.forEach((x, index, list) => {
		Request(x, (error, response, body) => {
			let data = JSON.parse(body);
			list[index] = data.name;
			gotten++;
			if (gotten == list.length)
				console.log(list.join("\n"));
		});
	});
});
