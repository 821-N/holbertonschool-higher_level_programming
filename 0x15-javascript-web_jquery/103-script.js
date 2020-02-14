/* eslint-disable */
$(function($) {
	function update() {
		$.getJSON(
			"https://www.fourtonfish.com/hellosalut/?lang=" +
				$("INPUT#language_code").val(),
			function(data) {
				$("DIV#hello").text(data.hello);
			}
		);
	}
	
	$("INPUT#btn_translate").click(update);
	$("INPUT#language_code").keypress(function(event) {
		if (event.which == 13)
			update();
	});
});
