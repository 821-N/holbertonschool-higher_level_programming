#!/usr/bin/node
/* eslint-disable */

const Request = require('request');

Request(process.argv[2].replace("films","people/18"), (error, response, body) => {
	console.log(JSON.parse(body).films.length);
});
