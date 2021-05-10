const api_url = "https://pokinaturalist-inaturalist.herokuapp.com/observations"
var existing_markers = [];

function get_creatures(lng, lat) {
    // Fetch creature information from our iNaturalist API
    $.ajax({
        url: `${api_url}?lat=${lat}&lng=${lng}`,
        type: "GET",
        dataType: 'json',
        success: display_creatures_on_map,
        error: failure,
    });
}

function markerAlreadyExists(marker) {
    // Check if marker has already been added to the map.
    if (!existing_markers.length) {
        return false;
    }

    for (j = 0; j < existing_markers.length; j++) {
        if (existing_markers[j].getLatLng().lat == marker.getLatLng().lat && existing_markers[j].getLatLng().lng == marker.getLatLng().lng) {
            return true;
        }
    }
    return false;
}

function display_creatures_on_map(result, status, xhr) {
    // Use results from GET request to create markers on the map representing the creatures
    var creatures_json = JSON.parse(JSON.stringify(result));
    var a = JSON.stringify(creatures_json);

    var creatures = creatures_json["results"];
    if (!creatures.length) {
        console.log("No creatures to display.");
        return;
    }

    // Iterate through results and plot creatures on map
    for (i = 0; i < creatures.length; i++) {
        var creature_marker = L.marker([creatures[i]["latitude"], creatures[i]["longitude"]]);

        if (markerAlreadyExists(creature_marker)) {
            continue;
        }

        creature_marker.addTo(map);
        var content = `<img src="${creatures[i]["photo"]}"><br><b>${creatures[i]["species_guess"].toUpperCase()}</b>\
                        <br><b><a href="${creatures[i]["wiki"]}" target="_blank">Learn More</a></b><br>\
                        <button type="button" class="btn btn-primary">Battle</button>`;
        creature_marker.bindPopup(content);
        existing_markers.push(creature_marker);
    }

}

function failure(result) {
    console.log("Failed request.");
    console.log(result);
}