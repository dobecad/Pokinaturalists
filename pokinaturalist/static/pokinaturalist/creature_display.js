const api_url = "https://pokinaturalist-inaturalist.herokuapp.com/observations"

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
        var creature_marker = L.marker([creatures[i]["latitude"], creatures[i]["longitude"]]).addTo(map);
        var content = `<img src="${creatures[i]["photo"]}"><br><b>${creatures[i]["species_guess"].toUpperCase()}</b>\
                        <br><b><a href="${creatures[i]["wiki"]}" target="_blank">Learn More</a></b>`;
        creature_marker.bindPopup(content);
    }

}

function failure(result) {
    console.log("Failed request.");
    console.log(result);
}