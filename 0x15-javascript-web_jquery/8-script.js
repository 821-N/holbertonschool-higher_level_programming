/* eslint-disable */
$.getJSON("https://swapi.co/api/films", function(data) {
	$.each(data.results, function(_, film) {
		$("UL#list_movies").append($("<li>").text(film.title));
	});
});
