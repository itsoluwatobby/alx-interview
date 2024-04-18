#!/usr/bin/node
/**
 * Write a script that prints all characters of a Star Wars movie:
 */
const request = require('request');

const index = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

request(filmURL + index, async (err, res, body) => {
  if (err) return console.error(err);

  const charURLList = JSON.parse(body).characters;

  for (const charURL of charURLList) {
    await new Promise((resolve, reject) => {
      request(charURL, (err, res, body) => {
        if (err) return console.error(err);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
