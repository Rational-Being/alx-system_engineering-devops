#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '/18/';

request(url, function (error, response, body) {
    if (error) console.log(error);
    else {
        const content = JSON.parse(body)
        const result = content.results;
        console.log(result.reduce((incr, movie) => {
            return movie.characters.find((character) => character.endsWith(characterId)) ? incr + 1 : incr;
        }, 0));

    }
});
