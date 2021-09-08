// 点击实现隐藏\显示功能
window.onload = function () {
  var obt = document.getElementById("btn-1");
  var odiv = document.getElementById("bar_1");
  var bodybg = document.getElementsByTagName("body")
  obt.onclick = function () {
    if (odiv.style.display == "none") {
      odiv.style.display = "block";
      obt.value = "隐藏模块";
    } else {
      odiv.style.display = "none";
      obt.value = "显示模块";
    }
  };
};
