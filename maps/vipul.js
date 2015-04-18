function initialize() {
  var mapOptions = {
    zoom: 14
  };
  var markers=[];
  var map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  var input = (
      document.getElementById('search'));
  /*map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);*/
  var searchBox = new google.maps.places.SearchBox((input));
  google.maps.event.addListener(searchBox, 'places_changed', function() {
    var places = searchBox.getPlaces();

    if (places.length == 0) {
      return;
    }
    for (var i = 0, marker; marker = markers[i]; i++) {
      //marker.setMap(null);
    }

    // For each place, get the icon, place name, and location.
    markers = [];
    var marker = new google.maps.Marker({
        map: map,
        icon: image,
        title: place.name,
        position: place.geometry.location
      });
    markers.push(marker);
    google.maps.Map(markers);
   }); 

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
        var options = {
        map: map,
        position: new google.maps.LatLng(21, 78),
        zoom:3,
      };
      map = new google.maps.Map(document.getElementById('map-canvas'),
      options);
      
      //var infowindow = new google.maps.InfoWindow(options);
      map.setCenter(options.position);   
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