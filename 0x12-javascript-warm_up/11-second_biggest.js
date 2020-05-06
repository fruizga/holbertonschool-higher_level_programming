#!/usr/bin/node
const Argus = process.argv.slice(2);
function compareNum (num1, num2) {
  return num1 - num2;
}
const cnt = Argus.length;
if (cnt === 0 || cnt === 1) {
  console.log(0);
} else {
  console.log(Argus.sort(compareNum)[cnt - 2]);
}
