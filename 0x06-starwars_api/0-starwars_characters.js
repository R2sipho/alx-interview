#!/usr/bin/env node

const axios = require('axios');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

(async () => {
  try {
    const response = await axios.get(url);
    const characters = response.data.characters;

    for (const characterUrl of characters) {
      const characterResponse = await axios.get(characterUrl);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error(error);
  }
})();

