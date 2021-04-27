



function weatherBallon( cityID ) {
	fetch('https://api.openweathermap.org/data/2.5/weather?id=' + 3873544+ '&appid=' + '641e6721ad2b0c1cc7c9245ab45ff281')  
	.then(function(resp) { return resp.json() }) // Convert data to json
	.then(function(data) {
		drawWeather(data);
	})
}
function drawWeather( d ) {
  var celcius = Math.round(parseFloat(d.main.temp)-273.15);
	var fahrenheit = Math.round(((parseFloat(d.main.temp)-273.15)*1.8)+32);
	
	document.getElementById('temp').innerHTML = celcius + '&deg;';
}

window.onload = function() {
	weatherBallon( 6167865 );
}





