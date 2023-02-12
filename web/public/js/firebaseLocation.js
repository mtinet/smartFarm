// GPS좌표 및 위치 리음 설정
let lat = 0;
let long = 0;
let label = "쥬디다무 집"

// Firebase 접근 정보
var config = {
  apiKey: "AIzaSyA4JNrHtS9pc6QaW8dtwATWhUhs0Ni8OBI",
  authDomain: "smartfarm-f867f.firebaseapp.com",
  databaseURL: "https://smartfarm-f867f-default-rtdb.firebaseio.com",
  projectId: "smartfarm-f867f",
  storageBucket: "smartfarm-f867f.appspot.com",
  messagingSenderId: "605663694333",
  appId: "1:605663694333:web:ae528fa94efc794d285d94",
  measurementId: "G-9C54BH4QG4"
};
firebase.initializeApp(config);
database = firebase.database();


// 지도 정보 가져오기
function initMap() {
  // 위치 정보 가져오기
  var refLocation = database.ref("location");
  refLocation.on("value", gotLocation, errData);

  function gotLocation(data) {
    console.log(data.val());
    // console.log(data.val()["lat"])
    // console.log(data.val()["long"])
    lat = data.val()["lat"]
    long = data.val()["long"]

    // console.log(lat, long)
    var seoul = { lat: lat, lng: long };
    var map = new google.maps.Map(
      document.getElementById('map'), {
        zoom: 12,
        center: seoul
      });

      new google.maps.Marker({
      position: seoul,
      map: map,
      label: label
    });
  }

  function errData(err) {
    console.log("Error!");
    console.log(err);
  }


}
