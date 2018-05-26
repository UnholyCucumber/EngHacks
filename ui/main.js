// $(document).ready(function(){
// 	//$("#getTest").text($.get("https://localhost:5000/functionTest/meme"));
// 	//console.log($.get("localhost:5000/functionTest/meme"));
// 	var meme = $.ajax({
// 		url: "http://localhost:5000/functionTest/meme",
// 		dataType: "json",
// 		sucess: function(result){
// 			console.log(result);
// 			console.log(typeof result);
// 		}
// 	}
// 		);
// 	//console.log(meme['hwat']);
// })
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $http) {

	var apiToken = "737f0946481560fccacc9ec4afd0c3c1"

    $http.get("http://localhost:5000/functionTest/meme")
    .then(function(result) {
        $scope.myWelcome = result.data.hwat[1];
        var test = result.data;
        console.log(test.hwat);
		console.log(typeof result);
    });

	$http.get("https://api.uwaterloo.ca/v2/courses.json?key=" + apiToken)
	.then(function(result){
		$scope.result = result

	});



});
