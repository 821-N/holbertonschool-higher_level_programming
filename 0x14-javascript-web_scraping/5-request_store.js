#!/usr/bin/node
/* eslint-disable */

const Request = require('request');
const Fs = require('fs');

Request(process.argv[2], (error, response, body) => {
	Fs.writeFile(process.argv[3], body, ()=>{});
});
