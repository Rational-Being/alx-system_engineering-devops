#!/usr/bin/node

const fs = require('fs');
const content = process.argv[3];
const filePath = process.argv[2];

fs.writeFile(filePath, content, 'utf-8', function (error, data) {
    if (error) console.log(error);
})
