#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) console.log('Missing size');
else {
  let v = '';
  for (let i = 0; i < size; i++) v += 'X';
  v.split('').forEach(() => console.log(v));
}
