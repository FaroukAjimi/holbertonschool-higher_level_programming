#!/usr/bin/node
const process = require('process');
const request = require('request');
request('https://swapi-api.hbtn.io/api/people/18/?format=json', function (error, response, body) {
  if (error) { throw error; }
  const jsn = JSON.parse(body);
  for (const key in jsn) { if (key === 'films') {console.log(jsn[key].length)}}
});
