#!/usr/bin/node
const Arg1 = parseInt(process.argv[2]);
if (Arg1) {
  console.log('My number: ' + Arg1);
} else {
  console.log('Not a number');
}
