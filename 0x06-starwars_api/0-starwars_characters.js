#!/usr/bin/node

const request = require('request');

// Define the Star Wars API base URL
const apiUrl = 'https://swapi-api.alx-tools.com/api';

// Function to fetch characters from a specific movie
function getCharactersInMovie (movieId) {
  const filmUrl = `${apiUrl}/films/${movieId}/`;

  request(filmUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const filmData = JSON.parse(body);
      const characters = filmData.characters;

      if (characters.length === 0) {
        console.log('No characters found for this movie.');
      } else {
        console.log(`Characters in the movie "${filmData.title}":`);
        const characterNames = [];

        // Fetch character names in the order they appear in the movie
        characters.forEach((characterUrl, index) => {
          request(characterUrl, (error, response, characterBody) => {
            if (!error && response.statusCode === 200) {
              const characterData = JSON.parse(characterBody);
              characterNames.push(characterData.name);
              if (index === characters.length - 1) {
                console.log(characterNames.join('\n'));
              }
            } else {
              console.error(`Error fetching character data: ${error}`);
            }
          });
        });
      }
    } else {
      console.error(`Error fetching movie data: ${error}`);
    }
  });
}

// Check if a movie ID is provided as a command-line argument
const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a movie ID as a command-line argument.');
} else {
  getCharactersInMovie(movieId);
}
