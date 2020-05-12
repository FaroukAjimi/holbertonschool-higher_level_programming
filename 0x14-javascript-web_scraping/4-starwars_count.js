#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) { throw error; }
  const jsn = JSON.parse(body);
  let z = 0;
  for (let i = 0; jsn.results[i]; i++) {
    if (jsn.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) { z++; }
  }
  console.log(z);
});
