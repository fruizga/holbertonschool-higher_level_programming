#!/usr/bin/node

const argues = process.argv.slice(2);
const fs = require('fs');
fs.writeFile(argues[0], argues[1], function (err) {
  if (err) {
    console.log(err);
  }
});
