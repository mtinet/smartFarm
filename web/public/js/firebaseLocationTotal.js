  // This code was written by Juhyun Kim.

  let database = null;
  let map = null;

  function initMap() {
    // Firebase 접근 정보
    var config = {
      apiKey: "AIzaSyD_g47-C90bK_BCD6DH56Z5DuHh_lf93x4",
      authDomain: "smartfarmlocation.firebaseapp.com",
      databaseURL: "https://smartfarmlocation-default-rtdb.firebaseio.com",
      projectId: "smartfarmlocation",
      storageBucket: "smartfarmlocation.appspot.com",
      messagingSenderId: "580782206031",
      appId: "1:580782206031:web:a3af204e4ea23fd67e8e3a",
      measurementId: "G-GB1HRVK5RH"
    };

    // Firebase 앱 초기화
    if (!firebase.apps.length) {
      firebase.initializeApp(config);
    }

    database = firebase.database();

    // 위치 정보 가져오기
    var refLocations = database.ref();
    refLocations.on("value", gotLocations, errData);

    // 지도 생성
    map = new google.maps.Map(document.getElementById("map"), {
      zoom: 10,
      center: { lat: 37.5, lng: 127 },
    });
  }

  function gotLocations(data) {
    var locations = data.val();
    createMarkers(locations, map);
  }

  function errData(err) {
    console.log("Error!");
    console.log(err);
  }


  function createMarkers(locations, map) {
  var keys = Object.keys(locations);
  for (var i = 0; i < keys.length; i++) {
    var id = keys[i];
    var location = locations[id];
    var latlng = new google.maps.LatLng(location.lat, location.long);

    var label = id;
    var smartFarmInfo = location.smartFarm;
    var content = document.createElement("div");
    var labelDiv = document.createElement("div");

    // id 부분만 진하게 표시
    var labelDiv = document.createElement("div");
    labelDiv.innerHTML = label;
    labelDiv.style.fontWeight = "bold";
    labelDiv.style.color = "#000000"; // id 색상 변경
    labelDiv.style.padding = "5px";
    labelDiv.style.marginBottom = "10px";
    labelDiv.style.boxShadow = "2px 2px 2px rgba(0, 0, 0, 0.3)"; // 테두리에 음영 추가
    content.appendChild(labelDiv);

    var smartFarmTable = document.createElement("table");
    var keys2 = Object.keys(smartFarmInfo);
    // 테이블 생성 루프
    for (var j = 0; j < keys2.length; j++) {
      var key = keys2[j];
      var value = smartFarmInfo[key];
      var row = document.createElement("tr");
      var keyCell = document.createElement("td");
      var valueCell = document.createElement("td");
      keyCell.innerHTML = key;
      valueCell.innerHTML = value;

      // 원하는 스타일을 적용
      if (key === "currentTime") {
        valueCell.style.color = "#000000";  // 검정색
        valueCell.style.fontFamily = "Arial, sans-serif"; // 글꼴 변경
      } else if (key === "-fan-" || key === "-led-") {
        valueCell.style.color = "#FFA500";  // 주황색
        valueCell.style.fontFamily = "Arial, sans-serif"; // 글꼴 변경
      } else if (key === "mois" || key === "temp" || key === "light" || key === "humi") {
        valueCell.style.color = "#008000"; // 초록색
        valueCell.style.fontFamily = "Arial, sans-serif"; // 글꼴 변경
      }

      // keyCell의 색상을 검정색으로 변경
      if (key === "currentTime") {
        keyCell.style.color = "#000000";  // 검정색
        keyCell.style.fontFamily = "Arial, sans-serif"; // 글꼴 변경
      } else if (key === "-fan-" || key === "-led-") {
        keyCell.style.color = "#FFA500";  // 주황색
        keyCell.style.fontFamily = "Arial, sans-serif"; // 글꼴 변경
      } else if (key === "mois" || key === "temp" || key === "light" || key === "humi") {
        keyCell.style.color = "#008000"; // 초록색
        keyCell.style.fontFamily = "Arial, sans-serif"; // 글꼴 변경
      }

      row.appendChild(keyCell);
      row.appendChild(valueCell);
      smartFarmTable.appendChild(row);
    }
    content.appendChild(smartFarmTable);

    var marker = new google.maps.Marker({
      position: latlng,
      map: map,
      label: label,
      content: content,
    });

    // 정보창 생성
    var infoWindow = new google.maps.InfoWindow();
    // 정보창 스타일 변경
    infoWindow.setContent(content);
    var infoWindowContent = infoWindow.getContent();
    var infoWindowDiv = infoWindowContent.firstChild;
    infoWindowDiv.style.fontSize = "14px";
    infoWindowDiv.style.fontWeight = "bold";
    infoWindowDiv.style.color = "#000000";

    // 마커에 이벤트 리스너 추가
    marker.addListener("mouseover", function() {
      infoWindow.setContent(this.content);
      infoWindow.open(map, this);
    });
    marker.addListener("mouseout", function() {
      infoWindow.close();
    });
    // 마커에 터치 이벤트 리스너 추가
    marker.addListener("click", function() {
      infoWindow.setContent(this.content);
      infoWindow.open(map, this);
    });
  }
}
