# -*- coding: utf-8 -*-
"""
@version: 3.8.3
@author: Yamisora
@file: 原神立绘爬虫.py
"""
import urllib.request
import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34 '}
char_url = 'https://wiki.biligame.com/ys/角色'
response = requests.get(char_url, headers=header)
soup = BeautifulSoup(response.text, 'lxml')
tabs = soup.find_all('div', class_='floatnone')
names = []
for tab in tabs:
    names.append(tab.find('a', href=True)['title'])
names = set(names)

pre_url = 'https://wiki.biligame.com/ys/文件:'
su_url = '立绘.png'
# su_url = '抽卡立绘.png'
for name in names:
    print('正在下载' + name + '立绘')
    url = pre_url + name + su_url
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'lxml')
    fil = soup.find('div', class_='fullImageLink')
    image_url = fil.find('a', href=True)['href']
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-agent',
         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34 ')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(image_url, name + '.png')
