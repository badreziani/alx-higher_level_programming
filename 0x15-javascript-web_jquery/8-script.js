$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const moviesTitles = data.results.map(function (movie) {
    return `<li>${movie.title}</li>`;
  });
  $('ul#list_movies').append(moviesTitles);
});
