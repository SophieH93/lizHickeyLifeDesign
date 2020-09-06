/**
 * Initilizes the map from Google Maps API
 */
function initMap() {
    const mapRef = document.getElementById('map');
    const contentRef = document.getElementById('info-window-content');
    const lifedesignlocation = { lat:  53.3018639, lng: -6.1788342 };
    const map = new google.maps.Map(mapRef, { zoom: 13, center: lifedesignlocation });
    const marker = new google.maps.Marker({
        position: lifedesign,
        map: map,
        title: 'lifedesign',
    }); 
};