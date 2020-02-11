#!/usr/bin/node
/* eslint-disable */

const Request = require('request');

Request("http://swapi.co/api/films/"+process.argv[2], (error, response, body) => {
	console.log(JSON.parse(body).title);
});

// Axios > Request
// 3 dependencies vs 48
//const Axios = require('axios');
//Axios.get("http://swapi.co/api/films/"+process.argv[2]).then((response) => {
//	console.log(response.data.title);
//});
