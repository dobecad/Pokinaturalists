// JS functionality to get geolocation data from user

var map;
var userMarker;
var userIcon;
var mapboxAccessToken;
var watchId;
var maxZoomLevel = 18;     // Lower number = more zoomed out
var minZoomLevel = 15;
var maxAge = 25000;
var timeUntilTimeout = 20000;
var timeBetweenCreatureRefresh = 120000 // 2 minutes in milliseconds
var trainerImg = "/static/pokinaturalist/img/trainer.png";

function getLocation(token) {
    if (navigator.geolocation) {
        mapboxAccessToken = token;
        $(document).ready(navigator.geolocation.getCurrentPosition(showPosition, error));
    } else { 
        alert("Geolocation is not supported by this browser.");
        console.log("Geolocation not enabled on device.");
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
    }).fitWorld();

    // Play animation that zooms in on user's location only once
    if (localStorage.getItem("run_once") === null) {
        map.flyTo(latlng, maxZoomLevel);

        // After zoom animation is finished, begin continuosly tracking user device location
        map.on('zoomend', function() {
            trackUserLocation();
            map.setMinZoom(minZoomLevel);
        });

        localStorage.setItem("run_once", true);
    } else {
        map.setView(latlng, maxZoomLevel);
        map.setMinZoom(minZoomLevel);
        trackUserLocation();
    }

    // This loads the tile's to the map from MapBox.
    // Be aware that the tiles will be queried from MapBox several times when the user first loads the page
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        maxZoom: maxZoomLevel,
        id: 'mapbox/outdoors-v11',
        tileSize: 512,
        zoomOffset: -1,
        reuseTiles: true,
        unloadInvisibleTiles: true,
        accessToken: mapboxAccessToken
    }).addTo(map);

    // Add a marker to the map which identifies user's location
    userIcon = L.icon({
        iconUrl: trainerImg,
        iconSize: [45, 50],
        iconAnchor: [25, 50],
        popupAnchor: [-25, -50]
    });
    userMarker = L.marker(latlng, {icon: userIcon}).addTo(map);

    get_creatures(userMarker.getLatLng().lng, userMarker.getLatLng().lat);

    // Fetch new creatures after timeBetweenCreatureRefresh time passes
    setInterval(function() {
        get_creatures(userMarker.getLatLng().lng, userMarker.getLatLng().lat);
    }, timeBetweenCreatureRefresh);

    // Disable user from changing zoom
    // map.touchZoom.disable();
    // map.doubleClickZoom.disable();
    // map.scrollWheelZoom.disable();
    // map.boxZoom.disable();
    // map.keyboard.disable();

}

function trackUserLocation() {
    // Set up geolocation tracking
    const options = {
        enableHighAccuracy: false,
        maximumAge: maxAge,
        timeout: timeUntilTimeout
    };
    watchId = navigator.geolocation.watchPosition(success, error, options);

    map.on("zoom", function() {
        map.setView(userMarker.getLatLng());
    });

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
    map.setView(newCoords);
}

function error(error) {
    console.log("Failed to update user location.");
    console.log("Error: ", error.code);
}
