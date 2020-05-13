#!/usr/bin/node

const fs = require('request');
fs(process.argv[2], { json: true }, (err, response, body) => {
  if (err) { console.log(err); } else {
    const final = {};
    for (const wr of body) {
      if (wr.completed) {
        if (final[wr.userId]) {
          final[wr.userId] += 1;
        } else {
          final[wr.userId] = 1;
        }
      }
    }
    console.log(final);
  }
});
