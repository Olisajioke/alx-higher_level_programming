/* eslint-disable */
// Fetches movie titles and lists them in UL#list_movies
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    data.results.forEach(function (movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
/* eslint-enable */
