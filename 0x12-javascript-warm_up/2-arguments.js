#!/usr/bin/node
const len = process.argv.length - 2;
const print = console.log;

if (!len) print('No arguments');
if (len === 1) print('Argument found');
if (len > 2) print('Argument found');
