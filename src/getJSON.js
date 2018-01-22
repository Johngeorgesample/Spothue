var getJSON = function(url, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);
  xhr.responseType = 'json';
  xhr.onload = function() {
    var status = xhr.status;
    if (status === 200) {
      callback(null, xhr.response);
    } 
    else {
      callback(status, xhr.response);
    }
  };
  xhr.send();
};

getJSON('http://127.0.0.1:5000/',
function(err, data) {
  if (err !== null) {
    alert('Something went wrong: ' + err);
  } 
  else {
    console.log(data.album.images[0].url);
    document.getElementById('myImg').src=data.album.images[0].url;

    var img = new Image();
    img.onload = function () {
      var colorThief = new ColorThief();
      console.log(colorThief.getPalette(img, 4)); //4 = number of colors to return

      //---
      var r = colorThief.getPalette(img, 4)[0][0];
      var g = colorThief.getPalette(img, 4)[0][1];
      var b = colorThief.getPalette(img, 4)[0][2];
      document.getElementById('color-one').style.backgroundColor = 'rgb(' + r + ',' + g + ',' + b + ')';

      var r = colorThief.getPalette(img, 4)[1][0];
      var g = colorThief.getPalette(img, 4)[1][1];
      var b = colorThief.getPalette(img, 4)[1][2];
      document.getElementById('color-two').style.backgroundColor = 'rgb(' + r + ',' + g + ',' + b + ')';

      var r = colorThief.getPalette(img, 4)[2][0];
      var g = colorThief.getPalette(img, 4)[2][1];
      var b = colorThief.getPalette(img, 4)[2][2];
      document.getElementById('color-three').style.backgroundColor = 'rgb(' + r + ',' + g + ',' + b + ')';

      var r = colorThief.getPalette(img, 4)[3][0];
      var g = colorThief.getPalette(img, 4)[3][1];
      var b = colorThief.getPalette(img, 4)[3][2];
      document.getElementById('color-four').style.backgroundColor = 'rgb(' + r + ',' + g + ',' + b + ')';
     
    };
    img.crossOrigin = 'Anonymous';
    img.src = document.getElementById('myImg').src;
  }
});