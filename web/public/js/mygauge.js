var gauge1 = Gauge(
  document.getElementById("gauge1"),
  {
    max: 100,
    value: 50,
    color: function(value) {
      if(value < 20) {
        return "#5ee432";
      }else if(value < 40) {
        return "#fffa50";
      }else if(value < 60) {
        return "#f7aa38";
      }else {
        return "#ef4655";
      }
    }
  }
);
var gauge2 = Gauge(
  document.getElementById("gauge2"),
  {
    max: 50,
    value: 25,
    color: function(value) {
      if(value < 10) {
        return "#5ee432";
      }else if(value < 20) {
        return "#fffa50";
      }else if(value < 30) {
        return "#f7aa38";
      }else {
        return "#ef4655";
      }
    }
  }
);
var gauge3 = Gauge(
  document.getElementById("gauge3"),
  {
    max: 100,
    value: 50,
    color: function(value) {
      if(value < 20) {
        return "#5ee432";
      }else if(value < 40) {
        return "#fffa50";
      }else if(value < 60) {
        return "#f7aa38";
      }else {
        return "#ef4655";
      }
    }
  }
);

(function loop() {
  var value1 = Math.random() * 100,
      value2 = Math.random() * 100,
      value3 = Math.random() * 100;

  gauge1.setValueAnimated(value1, 1.5);
  gauge2.setValueAnimated(value2, 1.5);
  gauge3.setValueAnimated(value3, 1.5);

  window.setTimeout(loop, 3000);
})();
