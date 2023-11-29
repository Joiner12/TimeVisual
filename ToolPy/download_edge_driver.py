# -*- coding:utf-8 -*-
import os, re, requests, shutil, zipfile, io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *

# 定义全局路径
global_config = {
    "edge_path": r"C:\Program Files (x86)\Microsoft\Edge\Application",
    "dirver_path": r"D:\Code\TimeVisual\ToolPy\driver",
}


class DownloadEdgeDriver:
    version_info = str()

    def __init__(self) -> None:
        version = self._CheckVersion()
        # 需要更新Edge驱动匹配当前版本
        if version:
            self._UpdateDriver()
            # print("需要更新Edge驱动匹配当前版本:", version)
        else:
            pass
            # print("new 得很")

    def GetVersionInfo(self):
        return self.version_info

    def _UpdateDriver(self):
        # 版本链接
        url = (
            r"https://msedgedriver.azureedge.net/"
            + self.version_info
            + r"/edgedriver_win64.zip"
        )

        # 发送 HTTP GET 请求获取文件内容
        response = requests.get(url)
        if response.status_code == 200:
            # 下载目录
            download_dir = global_config["dirver_path"]
            # 删除原有驱动文件
            pre_driver = os.path.join(download_dir, "msedgedriver.exe")
            if os.path.isfile(pre_driver):
                os.remove(pre_driver)
                # print("删除原有驱动文件:", pre_driver)
            # 将文件内容写入内存中
            file = io.BytesIO(response.content)
            # 解压缩文件
            with zipfile.ZipFile(file) as zip_file:
                # 解压缩到下载目录下
                zip_file.extractall(download_dir)
                # print("Edge版本:", self.version_info, "下载完成")
        else:
            pass
            # print('文件下载失败')

    # 检查Edge版本信息
    def _CheckVersion(self):
        edge_version = str()
        try:
            EDGE = {
                "browserName": "MicrosoftEdge",
                "version": "",
                "platform": "WINDOWS",
                "ms:edgeOptions": {
                    "extensions": [],
                    "args": [
                        "--headless"
                        # '--disable-gpu',
                        # '--remote-debugging-port=9222',
                    ],
                },
            }
            browser = webdriver.Edge(
                executable_path=r"D:\Code\TimeVisual\ToolPy\driver\msedgedriver.exe",
                capabilities=EDGE,
            )
            browser.close()
        except SessionNotCreatedException as msg:
            reg = re.search(
                "(.*)Current browser version is (.*) with", str(msg)
            )  # 识别并匹配Exception信息中出现的版本号
            edge_version = reg.group(2)  # 获得版本号
            # print(edge_version)
        self.version_info = edge_version
        return edge_version

    # 解析软件安装文件获取版本信息
    def _ParseVersionNum(self):
        config_file = os.path.join(
            global_config["edge_path"], "msedge.VisualElementsManifest.xml"
        )
        config_file_copy = os.path.join(
            global_config["dirver_path"], "msedge.VisualElementsManifest.xml"
        )
        # 拷贝文件
        shutil.copy(config_file, config_file_copy)
        file_content = str()
        version = str()
        # 读取文件内容
        try:
            with open(self.config_file_copy, "r") as f:
                file_content = f.read()
        except:
            print("copy file failed\n")
            return version
        # 使用正则表达式匹配版本号
        match = re.search(r"(\d+\.\d+\.\d+\.\d+)", file_content)

        if match:
            version = match.group(1)
        return version


if __name__ == "__main__":
    ded = DownloadEdgeDriver()
