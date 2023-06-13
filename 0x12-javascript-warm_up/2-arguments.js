#!/usr/bin/node
const len = process.argv.length - 2;
const print = console.log;

<<<<<<< HEAD
if (!len) print('No argument');
if (len === 1) print('Argument found');
if (len > 1) print('Arguments found');
=======
if (!len) print('No arguments');
if (len === 1) print('Argument found');
if (len > 2) print('Argument found');
>>>>>>> e418875ed53b3ff0a6866a31c540663edca7ab75
