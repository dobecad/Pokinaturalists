// JS functionality to get geolocation data from user

var map;
var userMarker;
var waitInSeconds = 15;
var waitInMilliseconds = waitInSeconds * 1000;
var mapboxAccessToken;
var watchId;
var zoomLevel = 18;

function getLocation(token) {
    if (navigator.geolocation) {
        mapboxAccessToken = token;
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        alert("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    // Get user coordinates after user accepts
    var latlng = L.latLng(position.coords.latitude, position.coords.longitude);

    // Generate map from leaflet.js
    map = L.map('map', {
        center: latlng,
        dragging: false,
        zoomControl: false
    }).setView([0, 0], 0);

    // Play animation that zooms in on user's location
    map.flyTo(latlng, zoomLevel);

    // This loads the tile's to the map from MapBox.
    // Be aware that the tiles will be queried from MapBox several times when the user first loads the page
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        maxZoom: zoomLevel,
        id: 'mapbox/outdoors-v11',
        tileSize: 512,
        zoomOffset: -1,
        reuseTiles: true,
        unloadInvisibleTiles: true,
        accessToken: mapboxAccessToken
    }).addTo(map);

    // Add a marker to the map which identifies user's location
    userMarker = L.marker(latlng).addTo(map);

    // Disable user from changing zoom
    map.touchZoom.disable();
    map.doubleClickZoom.disable();
    map.scrollWheelZoom.disable();
    map.boxZoom.disable();
    map.keyboard.disable();

    // After zoom animation is finished, begin continuosly tracking user device location
    map.on('zoomend', trackUserLocation);
}

function trackUserLocation() {
    // Set up geolocation tracking
    const options = {
        enableHighAccuracy: false,
        maximumAge: 25000,
        timeout: 20000
    };
    console.log("Starting watchPosition.");
    watchId = navigator.geolocation.watchPosition(success, error, options);

}

function stopTrackingLocation() {
    // Stop watchPosition from tracking device location
    navigator.geolocation.clearWatch(watchId);
}

function success(position) {
    // Update users coordinates, and change marker position
    var newCoords = L.latLng(position.coords.latitude, position.coords.longitude);
    console.log("New coords: ", newCoords.toString());
    userMarker.setLatLng(newCoords);
    map.setView(newCoords, zoomLevel);
}

function error(error) {
    console.log("Failed to update user location.");
    console.log("Error: ", error);
}
