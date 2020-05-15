$(document).ready(function(){
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, status) => {
  if (status === 'success') {
    for (const movie of data.results) {
        $('ul#list_movies').append($('<li></li>').text(movie.title));
    }
  }
  });
});
