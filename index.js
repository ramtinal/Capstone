function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    var d = today.getDate();
    var o = today.getMonth();
    var y = today.getFullYear();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('time').innerHTML =
    y + "/" + (o + 1) + "/" + d + " " + h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
  }
  function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
  }