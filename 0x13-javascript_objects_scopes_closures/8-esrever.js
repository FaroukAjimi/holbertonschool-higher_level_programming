#!/usr/bin/node
exports.esrever = function (list) {
  let aux = 0;
  let y = list.length - 1;
  for (let i = 0; i < y; i++) {
    aux = list[i];
    list[i] = list[y];
    list[y] = aux;
    y--;
  }
  return (list);
};
