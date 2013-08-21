var map;

function initialize() {
	var mapOptions = {
		zoom: 8,
		center: new google.maps.LatLng(-34.397, 150.644),
		mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    google.maps.event.addListener(map, 'click', function(event) {
	    getTweetsByGeoTag(event.latLng);
    });
}

function getTweetsByGeoTag(geotag) {

	geotagString = geotag.toString().replace('(','').replace(')','').split(',');
	lat = geotagString[0];
	lng = geotagString[1];
	term = $('#twitter-search').find('input[type=text]').val()

	$.get("/tweets", { term: term, lat: lat, lng: lng })
	.done(function(data) {
		data = $.parseJSON(data);	
	    updateTweets(data.tweets);
	});
}

function updateTweets(data) {
	content = "";
	for (var i = 0; i < data.length; i++) {
		
		content += '<div id="single-tweet">' + data[i] + '</div>';
	}
	$('#tweets').html(content);
}

$(document).ready(function() {
	google.maps.event.addDomListener(window, 'load', initialize);
});

