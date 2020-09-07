function initMap() {

        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 3,
          center: {lat: 53.1424, lng: 7.6921}
        });

        var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        var markers = locations.map(function(location, i) {
          return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
          });
        });

        // Add a marker clusterer to manage the markers.
        var markerCluster = new MarkerClusterer(map, markers,
            {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
      }
      var locations = [
        {lat: 53.350140, lng: -6.266155},  // Dublin 
        {lat: 52.489471, lng: -1.898575}, //  Birmingham 
        {lat: 51.260197, lng: 4.402771}, //  Belgium 
        {lat: 54.966667, lng:  -1.600000}, //  Newcastle 
        {lat: 48.864716, lng:  2.349014}, //  France 
        {lat: 45.9432, lng: 24.9668}, // Romania 
        {lat: 37.983810, lng: 23.727539}, // Greece 
        {lat: 64.128288, lng: -21.827774}, // Iceland 
        {lat: 41.902782, lng: 12.496366}, // Italy 
        {lat: 40.078072, lng: 9.283447}, // Sardinia 
        {lat: 33.738045, lng: 73.084488}, // Islamabad, Pakistan
        {lat: 50.073658, lng: 14.418540}, // Prague
        {lat: 52.237049, lng:  21.017532}, // Poland
        {lat: 33.233334, lng: -8.500000}, //  El Jadida
        {lat: 43.651070, lng: -79.347015}, // Toronto
        {lat: 34.052235, lng: -118.243683}, // LA
        {lat:38.84078, lng: 0.10574}, // Denia, Spain
        {lat: 58.298584, lng:  12.961619}, // Sweden
        {lat: 47.05048, lng:  8.30635}, // Switzerland 
        {lat: 41.015137, lng: 28.979530}, // Turkey 
        {lat: 15.81047, lng: 102.02881}, // Chaiyaphum, Thailand 
        {lat: 52.078663, lng: 4.288788}, // The Hague, Netherlands 
        {lat: 59.911491, lng: 10.757933}, // Norway
        {lat: 35.917973, lng: 14.409943}, // Malta
      ]