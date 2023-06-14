#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const row = new Array(this.width);
    row.fill('X');
    for (let i = 0; i < this.height; i++) console.log(row.join(''));
  }
}

module.exports = Rectangle;
