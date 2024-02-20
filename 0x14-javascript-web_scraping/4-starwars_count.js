#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';

request(url, funtion (error, rsponse, body) {
    if (error) console.log(error);
    else {
        const content = JSON.parse(body)
        const result = content.results;
        console.log(results.reduce((incr, movie) => {
            return movie.characters.find((character) => character.endsWith(characterId))
            ? incr + 1 : count ;
        }, 0));

    }
});