// home/js/custom_map.js

// NOTE: Building leaftletJS map for displaying registered users.


// get current user location.
const myLocation = JSON.parse(document.getElementById("myLocation").textContent)


// get all registered user data.
// get user data parsed down from django and convert to object.
const dataString = JSON.parse(document.getElementById("data").textContent);
const users = JSON.parse(dataString);


var registeredUsers = [
    ...users
];


// Map view (pan to my location).
var map = L.map("map").setView(myLocation.split(","), 3);


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


const profileString = (username, homeAddress, phoneNumber, coordinates) => {
    /*
    * NOTE: returns a string displaying all user information.
    *
    * @params
    *   username - user's username.
    *   homeAddress - user's home address.
    *   phoneNumber - user's phone number.
    *   coordinates - user's coordinates (Type: array with latitude and longitude)
    */
    return(`<span class='font-semibold'>Profile</span><br><span class='text-sm'>Username: ${username}</span><br><span class='text-sm'>Home address: ${homeAddress}</span><br><span class='text-sm'>Phone number: ${phoneNumber}</span><br><span class='text-sm'>Location: ${coordinates}</span>`)
}


for (var i = 0; i < registeredUsers.length; i++) {
    // if user location is empty don't display.
    if(registeredUsers[i].location.length > 0){
        let username = registeredUsers[i].username; // get username.
        let homeAddress = registeredUsers[i].home_address; // get username.
        let phoneNumber = registeredUsers[i].phone_number; // get phone number.
        let coordinates = registeredUsers[i].location.split(","); // array with latt and long values (get location/coordinates).

        // place user info in html tags (UI purpose).
        const profile = profileString(username, homeAddress, phoneNumber, coordinates);  
        marker = new L.marker(coordinates)
        .bindPopup(profile)
        .addTo(map);
    }
  }

