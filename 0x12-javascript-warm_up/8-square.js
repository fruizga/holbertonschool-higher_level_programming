#!/usr/bin/node
const sizeOfSquare = parseInt(process.argv[2]);
if (sizeOfSquare) {
  for (let row = 0; row < sizeOfSquare; row++) {
    for (let column = 0; column < sizeOfSquare; column++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
