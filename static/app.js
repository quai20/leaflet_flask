var map = L.map('lmap').setView([48, -50], 3);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var clicked = 0;
map.on('click', function (e) {            
    if (clicked ==1 ) {        
        domesomethingwithlatlon(e.latlng.lat, e.latlng.lng)
        $('.leaflet-container').css('cursor', '');
        clicked = 0;        
    }        
});

function dosomething() {
    clicked = 1;
    $('.leaflet-container').css('cursor', 'crosshair');
}

function domesomethingwithlatlon(lat, lon) {
    reqstring = 'lat='+lat.toString()+'&lon='+lon.toString()
    var marker = L.marker([lat, lon]).addTo(map);
    $.ajax({
        type: "GET",
        url: '/testfj',
        data: reqstring,
        contentType: 'application/json;charset=UTF-8',
        success: function (data) {            
            document.getElementById("toFill").innerHTML = data;
            dataarray = JSON.parse(data)
            console.log(dataarray);
        }
    });
}