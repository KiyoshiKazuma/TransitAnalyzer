import chromedriver_binary # nopa
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

class staion:
    def __init__(self,station_name,time_to_NIHONBASHI,transit_count_to_NIHONBASHI):
        self.station_name = station_name
        self.time_to_NIHONBASHI = time_to_NIHONBASHI
        self.transit_count_to_NIHONBASHI = transit_count_to_NIHONBASHI

    def print(self):
        print (self.station_name +" , "+self.time_to_NIHONBASHI+" , "+self.transit_count_to_NIHONBASHI)

    

# WebDriver のオプションを設定する
#options = webdriver.ChromeOptions()
#options.add_argument('--headless')

print('connectiong to remote browser...')
#driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

min=0
url=' https://realestate.navitime.co.jp/chintai/reachable?node=00004341&lower_term='+str(min)+'&higher_term='+str(min+10)+'&transit_limit=0#/'

driver.get(url)
time.sleep(3)

html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, "html.parser")

station_list_item_elements = driver.find_elements(By.CLASS_NAME,"station-info-area")
stations = []

for station_element in station_list_item_elements:
    station_tmp=staion(
        station_element.find_element(By.CLASS_NAME,"station-name").text,
        station_element.find_element(By.CLASS_NAME,"time").text,
        station_element.find_element(By.CLASS_NAME,"transit-count").text
    )
    station_tmp.print()
    stations.append(station_tmp)


# ブラウザを終了する
driver.quit()
