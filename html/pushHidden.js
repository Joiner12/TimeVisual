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
