$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (response) {
  for (let i = 0; response.results[i]; i++) {
    $('<li>' + response.results[i].title + '</li>').appendTo('UL#list_movies');
  }
});
