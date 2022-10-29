// home/js/custom_map.js

// NOTE: Building leaftletJS map for displaying registered users.

var latt = -34.04;
var long = 18.60;

// Map view.
var map = L.map("map").setView([latt, long], 10);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


// add markers to map.
var marker = L.marker([latt, long]).addTo(map);
