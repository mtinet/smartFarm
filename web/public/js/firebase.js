let mois = 100;
let temp = 50;
let light = 100;
let fanStatus = Boolean(false);
let ledStatus = Boolean(false);

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

// Firebase 정보 가져오기
var ref = database.ref("smartFarm");
ref.on("value", gotData, errData);

function gotData(data) {
  //console.log(data.val());
  var val = data.val();
  //console.log(val);
  var keys = Object.keys(val);
  //console.log(keys);
  var values = Object.values(val);
  //console.log(values);

  mois = val.mois;
  temp = val.temp;
  light = val.light;
  ledStatus = val.led;
  fanStatus = val.fan;
  //console.log(val.mois)
  //console.log(val.temp)
  //console.log(val.light)
  //console.log(ledStatus)
  //console.log(fanStatus)

  for (var i = 0; i < keys.length; i++) {
    var k = keys[i];
    //console.log(k)
    var v = values[i];
    //console.log(v);
    console.log(k + ":" + v);
  }

  // 버튼 상태 싱크
  if (ledStatus == false) {
    // ledButton 토글
    const ledButton = document.getElementById('ledButton');
    ledButton.style.filter = "brightness(50%)";
  } else {
    ledButton.style.filter = "brightness(100%)";
  }

  if (fanStatus == false) {
    // fanButton 토글
    const fanButton = document.getElementById('fanButton');
    fanButton.style.filter = "brightness(50%)";
  }else {
    fanButton.style.filter = "brightness(100%)";
  }
}

function errData(err) {
  console.log("Error!");
  console.log(err);
}

// led 상태를 확인하고 1(켜짐)이면 0(꺼짐)으로, 0(꺼짐)이면 1(켜짐)으로 Firebase 데이터를 업데이트 하고, 버튼 이미지의 밝기를 조정함
function ledOnOff() {
  if (ledStatus == false) {
    ledStatus = true;

    var ref = database.ref('smartFarm');
    ref.update({
      led: 1
    })

    // ledButton 토글
    const ledButton = document.getElementById('ledButton');
    ledButton.style.filter = "brightness(100%)";

  } else {
    ledStatus = false;

    var ref = database.ref('smartFarm');
    ref.update({
      led: 0
    })

    // fanButton 토글
    const ledButton = document.getElementById('ledButton');
    ledButton.style.filter = "brightness(50%)";
  }
  //console.log(ledStatus);
}

// fan 상태를 확인하고 1(켜짐)이면 0(꺼짐)으로, 0(꺼짐)이면 1(켜짐)으로 Firebase 데이터를 업데이트 하고, 버튼 이미지의 밝기를 조정함
function fanOnOff() {
  if (fanStatus == false) {
    fanStatus = true;

    var ref = database.ref('smartFarm');
    ref.update({
      fan: 1
    })

    // 토글 할 버튼 선택 (fanButton)
    const fanButton = document.getElementById('fanButton');
    fanButton.style.filter = "brightness(100%)";

  } else {
    fanStatus = false;

    var ref = database.ref('smartFarm');
    ref.update({
      fan: 0
    })

    // 토글 할 버튼 선택 (fanButton)
    const fanButton = document.getElementById('fanButton');
    fanButton.style.filter = "brightness(50%)";
  }
  //console.log(fanStatus);
}

// Firebase의 Realtime Database에 저장되어 있는 조도(light), 온도(temp), 습도() 정보를 가져와서 게이지 1, 2, 3에 뿌려서 표현하게 함, Firebase의 정보가 업데이트 되면 실시간으로 게이지가 변함
// 받아온 값의 수치에 따라서 초록-노랑-주황-빨강으로 게이지의 색깔이 변하게 세팅되어 있으므로, 색깔을 보고 수동으로 led와 fan을 조정하여 식물에 적용되는 환경을 조정할 수 있음
// 게이지 1은 조도를 나타내도록 세팅되었으므로 최대값을 100으로 지정함
var gauge1 = Gauge(
  document.getElementById("gauge1"),
  {
    max: 100,
    value: 0,
    color: function(value) {
      if(value < 20) {
        return "#5ee432"; // 초록
      }else if(value < 40) {
        return "#fffa50"; // 노랑
      }else if(value < 60) {
        return "#f7aa38"; // 주황
      }else {
        return "#ef4655"; // 빨강
      }
    }
  }
);

// 게이지 2는 온도를 나타내도록 세팅되었으므로 최대값을 50으로 지정함
var gauge2 = Gauge(
  document.getElementById("gauge2"),
  {
    max: 50,
    value: 0,
    color: function(value) {
      if(value < 10) {
        return "#5ee432"; // 초록
      }else if(value < 20) {
        return "#fffa50"; // 노랑
      }else if(value < 30) {
        return "#f7aa38"; // 주황
      }else {
        return "#ef4655"; // 빨강
      }
    }
  }
);
// 게이지 3은 수분를 나타내도록 세팅되었으므로 최대값을 100으로 지정함
var gauge3 = Gauge(
  document.getElementById("gauge3"),
  {
    max: 100,
    value: 0,
    color: function(value) {
      if(value < 20) {
        return "#5ee432"; // 초록
      }else if(value < 40) {
        return "#fffa50"; // 노랑
      }else if(value < 60) {
        return "#f7aa38"; // 주황
      }else {
        return "#ef4655"; // 빨강
      }
    }
  }
);

// 게이지에 값을 넣어주고, 3초마다 1.5의 반응속도로 리뉴얼함
(function loop() {
// 랜덤으로 값을 발생시켜 게이지의 동작을 테스트 할 때 사용
//  var value1 = Math.random() * 100,
//      value2 = Math.random() * 50, //온도 최대값은 50으로 조정되어 있으므로, 테스트도 0~50의 값으로 테스트 함
//      value3 = Math.random() * 100;

// Firebase Realtime Database로부터 넘어온 값을 각 게이지의 값에 넣어줌
  var value1 = light,
      value2 = temp,
      value3 = mois;

  gauge1.setValueAnimated(value1, 1.5);
  gauge2.setValueAnimated(value2, 1.5);
  gauge3.setValueAnimated(value3, 1.5);

  window.setTimeout(loop, 3000);
})();
