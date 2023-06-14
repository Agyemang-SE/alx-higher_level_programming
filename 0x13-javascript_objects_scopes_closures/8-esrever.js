#!/usr/bin/node
exports.esrever = function (list) {
  const invertedList = [];
  for (const l of list) invertedList.unshift(l);
  return invertedList;
};
