#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', funtion (error, data) {
    console.log(error || data);
})