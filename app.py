from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver. chrome. service import Service
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
service=Service(executable_path="C:/Users/Vishwajeet Kumbhar/OneDrive/Desktop/PYTHON/class128/PRO-C128-Student-Boilerplate-Code-main/chromedriver-win64/chromedriver.exe")
options=webdriver.ChromeOptions()
browser=webdriver.Chrome (service=service, options=options)

page = browser.get(START_URL)

time.sleep(10)

soup = BeautifulSoup(page.content,"html.parser")
temp_list = []
star_table = soup.find("table")
table_rows = star_table.find_all("tr")
for tr in table_rows:
    td= tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)


star_names = []
dist = []
mass = []
radius = []
lum = []
for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    dist.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    lum.append(temp_list[i][7])
headers = ["star_names","dist","mass","radius","lum"]
df = pd.DataFrame(list(zip(star_names,dist,mass,radius,lum)),columns = headers)
df.to_csv("stars.csv",index = True,index_label = "id")
                  
