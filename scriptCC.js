

function iniciarMap() {
      
      var marcadores = [
        [49.983299,18.9167, 'Altdorf'],
        [51.400001,17.466699, 'Althammer'],
        [50.026199,19.204099, 'Auschwitz I']
      ];
	var icon = {
    		url: "markShadow.png", // url
    		scaledSize: new google.maps.Size(60, 50), // scaled size
    		origin: new google.maps.Point(0,0), // origin
    		anchor: new google.maps.Point(0, 0) // anchor
	};
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 5,
        center: new google.maps.LatLng(50.0598058, 14.3255388),
        mapTypeId: google.maps.MapTypeId.ROADMAP
      });
      var infowindow = new google.maps.InfoWindow();
      var marker, i;

      for (i = 0; i < marcadores.length; i++) {  
        marker = new google.maps.Marker({
          position: new google.maps.LatLng(marcadores[i][1], marcadores[i][2]),
          map: map,
	icon: icon
        });

        google.maps.event.addListener(marker, 'click', (function(marker, i) {
          return function() {
            infowindow.setContent(marcadores[i][0]);
            infowindow.open(map, marker);
          }
        })(marker, i));
      }
    }
    google.maps.event.addDomListener(window, 'load', initialize);