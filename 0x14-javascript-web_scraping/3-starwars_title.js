#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films';

request(url + process.argv[2] + '/', (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        console.log(JSON.parse(body).title);
    }
});