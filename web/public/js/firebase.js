// 변수 선언
let humi = 0;
let temp = 0;
let light = 0;
let fanStatus = Boolean(false);
let ledStatus = Boolean(false);

// firebase를 javascript로 사용하기 위한 config  
// firebase 콘솔-프로젝트 개요-기어표시 클릭-프로젝트 설정-일반-내앱-앱 추가(세번 째 웹앱버튼을 눌러 추가)-생성되는 firebaseConfig 안의 내용만 복사해서 붙여넣음  
var config = {
  apiKey: "AIzaSyA4JNrHtS9pc6QaW8dtwATWhUhs0Ni8OBI",
  authDomain: "smartfarm-f867f.firebaseapp.com",
  databaseURL: "https://smartfarm-f867f-default-rtdb.firebaseio.com",
  projectId: "smartfarm-f867f",
  storageBucket: "",
  messagingSenderId: "605663694333",
};
firebase.initializeApp(config);
database = firebase.database();

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

  humi = val.humi;
  temp = val.temp;
  light = val.light;
  ledStatus = val.led;
  fanStatus = val.fan;
  //console.log(val.humi)
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
    // 토글 할 버튼 선택 (fanButton)
    const ledButton = document.getElementById('ledButton');
    ledButton.style.filter = "brightness(50%)";
  } else {
    ledButton.style.filter = "brightness(100%)";
  }

  if (fanStatus == false) {
    // 토글 할 버튼 선택 (fanButton)
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

function ledOnOff() {
  if (ledStatus == false) {
    ledStatus = true;

    var ref = database.ref('smartFarm');
    ref.update({
      led: 1
    })

    // 토글 할 버튼 선택 (sunButton)
    const ledButton = document.getElementById('ledButton');
    ledButton.style.filter = "brightness(100%)";

  } else {
    ledStatus = false;

    var ref = database.ref('smartFarm');
    ref.update({
      led: 0
    })

    // 토글 할 버튼 선택 (sunButton)
    const ledButton = document.getElementById('ledButton');
    ledButton.style.filter = "brightness(50%)";
  }
  //console.log(ledStatus);
}

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
