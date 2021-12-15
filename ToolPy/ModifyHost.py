# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 16:20:04 2021

@author: W-H
"""

from shutil import copyfile
import datetime
import os
import requests
import sys


class GithubHost():
    winHostsPath = 'C:\Windows\System32\drivers\etc\hosts'
    macHostsPath = '/etc/hosts'
    hostsDic = {'win32': winHostsPath, 'darwin': macHostsPath}
    dnsRefreshDic = {'win32': 'ipconfig /flushdns', 'darwin': ''}

    githubHostUrl = 'https://raw.hellogithub.com/hosts'
    googleHostUrl = ''

    def refreshHosts(self):
        # 备份原hosts文件
        hosts = self.hostsDic[sys.platform]
        self.backUpHosts(srcfile=hosts)

        # 获取并更新github新host内容
        self.updateHosts(hosts, self.githubHostUrl,
                         '# GitHub520 Host Start', '# GitHub520 Host End')

        # 获取并更新google新host内容
        # self.refreshHosts(hosts, self.googleHostUrl, '', '')

        # 刷新
        refreshCmd = self.dnsRefreshDic[sys.platform]
        os.system(refreshCmd)

    def updateHosts(self, hosts, hosturl, beginRowStr, endRowStr):
        # 删除原有内容
        self.removePartOfFile(hosts, beginRowStr, endRowStr)
        self.addHostsFromURL(hosts, hosturl)

    def removePartOfFile(self, file, beginRowStr, endRowStr):
        lines = []
        with open(file, 'r') as oldhosts:
            lineInRange = False
            for line in oldhosts:
                # 如果在beginRowStr 与 endRowStr 之间的，就不记录在新文件中
                if line.strip() == beginRowStr.strip():
                    lineInRange = True
                if not lineInRange and line.strip() != '':  # 删除空行
                    lines.append(line)
                if line.strip() == endRowStr.strip():
                    lineInRange = False

        with open(file, 'w') as newHosts:
            for line in lines:
                if len(line) != 0 and line is not os.linesep:
                    newHosts.write(line)

    def backUpHosts(self, srcfile):
        dstfile = srcfile + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        copyfile(src=srcfile, dst=dstfile)

    def addHostsFromURL(self, hostfile, hostsurl):
        '''从github项目地址：读取最新的github的IP记录'''
        with open(hostfile, 'a+') as fw:
            # 字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。
            # fw.write(os.linesep)
            fw.write(requests.get(hostsurl).text.strip())

    def update_manual(self, hostsurl=r'https://raw.hellogithub.com/hosts'):
        '''从githubhost 获取ip→输出到对话框→手动更新数据(文件权限问题)
        -----
        参数
        hostsurl:str
            服务器地址
        -----
        输出
            None
        '''

        ips = requests.get(hostsurl).text.strip()
        print(ips)
        os.startfile(r'C:\Windows\System32\drivers\etc')  # 打开文件夹窗口


if __name__ == "__main__":
    GithubHost().update_manual()
