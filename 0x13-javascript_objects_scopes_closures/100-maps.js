#!/usr/bin/node
const list = require('./100-main').list;
console.log(list);
const list2 = list.map(x => x * list.indexOf(x));
console.log(list2);
