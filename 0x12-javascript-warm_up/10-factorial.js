#!/usr/bin/node
const num = process.argv[2];
function factorial (num) {
  let i = 1;
  let result = 1;
  if (num) {
    while (i <= num) {
      result *= i;
      i++;
    }
  } else {
    return (1);
  }
  return (result);
}
console.log(factorial(num));
