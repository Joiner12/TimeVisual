// 点击实现隐藏\显示功能
window.onload = function () {
  var obt = document.getElementById("btn-pie");
  var odiv = document.getElementById("bar_1");
  obt.onclick = function () {
    if (odiv.style.display == "none") {
      odiv.style.display = "block";
    } else {
      odiv.style.display = "none";
    }
  };
};
window.onload = function () {
  var obt = document.getElementById("btn-pie");
  //获取iframe的window对象
  var topWin = window.top.document.getElementById("pie_iframe").contentWindow;
  //通过获取到的window对象操作HTML元素，这和普通页面一样
  var oiframe = (topWin.document.getElementById(
    "5a156e67104a454881553d9f547be356"
  ).style.visibility = "visible");
  obt.onclick = function () {
    if (odiv.style.display == "none") {
      odiv.style.display = "block";
    } else {
      odiv.style.display = "none";
    }
  };
};
window.onload = function () {
  var obt = document.getElementById("btn-bar");
  var odiv = document.getElementById("bar_1");
  obt.onclick = function () {
    if (odiv.style.display == "none") {
      odiv.style.display = "block";
    } else {
      odiv.style.display = "none";
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
