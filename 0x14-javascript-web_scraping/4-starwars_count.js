#!/usr/bin/node
const process = require('process');
const request = require('request');
let z = 0;
request(process.argv[2] + '/?format=json', function (error, response, body) {
  if (error) { throw error; }
  const jsn = JSON.parse(body);
  for (let i = 0; jsn.results[i]; i++) {
    if (jsn.results[i].characters.indexOf('https://swapi-api.hbtn.io/api/people/18/') >= 0) { z++; }
  }
  console.log(z);
});
