from bs4 import BeautifulSoup
import requests
from selenium import  webdriver
from webdriver_manager.chrome import  ChromeDriverManager
import csv
from itertools import zip_longest
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib import request
import re
# requests.options()
# result = requests.get("https://silverdragon.lifehacks.workers.dev/0:/")
# src = result.content
from pathlib import Path
def import_path(x=None):
    f = open(x ,  'r')
    src = f.read()
    f.close()
    return(src)
# src = f.read()

source_mp4 =  (import_path('/home/mohamed/Desktop/mp4.html'))

# print(src)
soup = BeautifulSoup(source_mp4,"html.parser")
courses_dir_list=[]
course_tittels_list = []
#text loop to get links in list
# courses_dirs= soup.find_all("a",attrs={'href' : re.compile("^(https(s)?:\/\/|www\.).*(\.mp4|\.pdf)$")})
course_tittels = soup.find_all("a",attrs={'href' : re.compile("^(https(s)?:\/\/|www\.).*(\.mp4|\.pdf)$")})
for i in range(len(course_tittels)):
    course_tittels_list.append(course_tittels[i].get('href'))
print(course_tittels_list)
def download_mp4(send_list):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # options = webdriver.ChromeOptions()
    # options.add_argument("download.default_directory=k:\\cloud-computing")
    # driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(20)
    for i in send_list:
        # time.sleep(3600)  # sleep for 1 second
        print(driver.get(i))
        time.sleep(1800)




    driver.implicitly_wait(20)

    driver.maximize_window()
    # time.sleep(100000000000000000000000)
    driver.implicitly_wait(20)

    time.sleep(1000000)
# download_mp4(course_tittels_list)
print( "create DIR" )
course_tittels_list1 = []
# soup = BeautifulSoup(src,"html.parser")
source_dir =  (import_path('/home/mohamed/Desktop/courses_dir.html'))
soup1 = BeautifulSoup(source_dir,"html.parser")
course_tittels1 = soup1.find_all("a",attrs={'href' : re.compile("^(https(s)?:\/\/|www\.).*(\.mp4|\.pdf)$")})
if len(course_tittels1):
    for i in range(len(course_tittels)):
        course_tittels_list1.append(course_tittels1[i].get('href'))
else:
    print(None)
print(course_tittels_list1)








