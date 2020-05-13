#!/usr/bin/node

const argues = process.argv.slice(2);
const request = require('request');
let cnt = 0;
request(argues[0], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const list = JSON.parse(body).results;
    for (const i of list) {
      for (const j of i.characters) {
        if (j.slice(-3) === '18/') {
          cnt++;
        }
      }
    }
    console.log(cnt);
  }
});
