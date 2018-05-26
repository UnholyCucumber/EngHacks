$(document).ready(function(){
	//$("#getTest").text($.get("https://localhost:5000/functionTest/meme"));
	//console.log($.get("localhost:5000/functionTest/meme"));
	var meme = $.ajax({
		url: "http://localhost:5000/functionTest/meme",
		dataType: "jsonp"
	}
		);
	console.log(meme);
})