
// This example adds a search box to a map, using the Google Place Autocomplete
// feature. People can enter geographical searches. The search box will return a
// pick list containing a mix of places and predicted search terms.

function initialize() {
  var mapOptions = {
    zoom: 14,
};

  var markers=[];
  var map = new google.maps.Map(document.getElementById('map-canvas'),
  mapOptions);

  
    // For each place, get the icon, place name, and location.
    
  // Try HTML5 geolocation
  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = new google.maps.LatLng(position.coords.latitude,
                                       position.coords.longitude);

      var infowindow = new google.maps.InfoWindow({
        map: map,
        position: pos,
        content: 'You are here'
      });

      map.setCenter(pos);
    }, function(error) {
      if(error.code==1)
      {
        
        window.location.assign("newstreet.html");
        /*var options = {
        map: map,
        position: new google.maps.LatLng(21, 78),
        zoom:3,
      };
      map = new google.maps.Map(document.getElementById('map-canvas'),
      options);
      
      //var infowindow = new google.maps.InfoWindow(options);
      map.setCenter(options.position);*/   
      }   
    });
    google.maps.event.addListener(map, "click", function eventer (event) {
      var latitude = event.latLng.lat();
      var longitude = event.latLng.lng();
      console.log( latitude + ', ' + longitude );
  });
  } else {
    // Browser doesn't support Geolocation
    handleNoGeolocation(false);
  }
}

function handleNoGeolocation(errorFlag) {
  if (errorFlag) {
    var content = 'Error: The Geolocation service failed.';
  } else {
    var content = 'Error: Your browser doesn\'t support geolocation.';
  }

  var options = {
    map: map,
    position: new google.maps.LatLng(60, 105),
    content: content
  };

  var infowindow = new google.maps.InfoWindow(options);
  map.setCenter(options.position);
}
google.maps.event.addDomListener(window, 'load', initialize);