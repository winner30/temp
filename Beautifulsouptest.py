from this import d
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
from time import sleep
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

try:
    shutil.rmtree(r"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
except FileNotFoundError:
    pass

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    print("driver 는" , driver)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    print("driver 이" , driver)

driver.get('https://seller.grip.show/login/idpw1')

sleep(0.5)
driver.find_element_by_name('id').send_keys('anneclassic')
sleep(0.5)
driver.find_element_by_name('password').send_keys('81rlagkdbs!')

driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/form/div[4]/button').click()

sleep(15)
response = urlopen('https://seller.grip.show/seller/product/1/')
soup = BeautifulSoup(response, 'html.parser')

tabletag = bs.find(name = "table", attrs = {"id" : "product-list"})

rows = tabletag.find("tbody").findAll("tr")

rowList = []
columnList = []

for i in range(0, len(rows)):
    columns = row[i].findAll("td")
    columnsLen = len(columns)
    for j in range(0, columnsLen):
        columnsList.append(columns[j].text)

    rowList.append(columnsList)
    columnList = []



#for anchor in soup.find_all('a'):
#    print(anchor.get('href','/'))

while(True):
    pass
#driver.implicitly_wait(10)


