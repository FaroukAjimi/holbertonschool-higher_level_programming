#!/usr/bin/node
const process = require('process');
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/?format=json', function (error, response, body) {
  if (error) throw error;
  const jsn = JSON.parse(body);
  for (var key in jsn) { if (key === 'title') console.log(jsn[key]); }
});
