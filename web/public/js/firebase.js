let humi = 0;
let temp = 0;
let light = 0;
let fanStatus = Boolean(false);
let ledStatus = Boolean(false);

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
