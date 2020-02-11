#!/usr/bin/node
/* eslint-disable */

const Request = require('request');

Request(process.argv[2], (error, response) => {
	console.log("code: "+response.statusCode);
});
