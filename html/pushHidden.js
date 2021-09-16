// 点击实现隐藏\显示功能
window.onload = function () {
  // bar button
  document.getElementById("btn-bar").onclick = function () {
    var odivPie = document.getElementById("bar_iframe");
    if (odivPie.style.display == "none") {
      odivPie.style.display = "block";
    } else {
      odivPie.style.display = "none";
    }
  };
  // pie button
  document.getElementById("btn-pie").onclick = function () {
    var odivPie = document.getElementById("pie_iframe");
    if (odivPie.style.display == "none") {
      odivPie.style.display = "block";
    } else {
      odivPie.style.display = "none";
    }
  };

  // geo button
  document.getElementById("btn-geo").onclick = function () {
    var odivPie = document.getElementById("geo_iframe");
    if (odivPie.style.display == "none") {
      odivPie.style.display = "block";
    } else {
      odivPie.style.display = "none";
    }
  };

  // line button
  document.getElementById("btn-line").onclick = function () {
    var odivPie = document.getElementById("line_iframe");
    if (odivPie.style.display == "none") {
      odivPie.style.display = "block";
    } else {
      odivPie.style.display = "none";
    }
  };
};

function adjustIframe() {
  var ifm = document.getElementById("pie_iframe");
  ifm.height = document.documentElement.clientHeight;
  ifm.width = document.documentElement.clientWidth;
  var ifm = document.getElementById("bar_iframe");
  ifm.height = document.documentElement.clientHeight;
  ifm.width = document.documentElement.clientWidth;
  var ifm = document.getElementById("geo_iframe");
  ifm.height = document.documentElement.clientHeight;
  ifm.width = document.documentElement.clientWidth;
}
