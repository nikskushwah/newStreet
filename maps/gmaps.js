function initialize() {
  var mapOptions = {
    zoom: 14,
  };

  var map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);
  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
    var pos = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);

    var infowindow = new google.maps.InfoWindow({
      map: map,
      position: pos,
      content: 'Right now you are here'
    });

    map.setCenter(pos);
    }, function() {
      handleNoGeolocation(true);
    });
    //this gives the latitude and longitude on clicking.
    google.maps.event.addListener(map, "click", function eventer (event) {
      var latitude = event.latLng.lat();
      var longitude = event.latLng.lng();
      console.log( latitude + ', ' + longitude );
  });
  } else {
    // Browser doesn't support Geolocation
    handleNoGeolocation(false);
   }
  //update what if user doesnot allow to track the location
    /*navigator.geolocation.getCurrentPosition(
    function (error) { 
      if (error.code == error.PERMISSION_DENIED)
          console.log("you denied me :-(");
          var infowindow = new google.maps.InfoWindow({
          map: map,
          position: new google.maps.LatLng(60,105),
          content: 'Track now'
    });*/
}
//when geolocation gives an error
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
  //this gives the latitude and longitude on clicking.
  google.maps.event.addListener(map, "click", function eventer (event) {
      var latitude = event.latLng.lat();
      var longitude = event.latLng.lng();
      console.log( latitude + ', ' + longitude );
  });
}
google.maps.event.addDomListener(window, 'load', initialize);


