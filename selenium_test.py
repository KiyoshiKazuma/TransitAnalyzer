import chromedriver_binary # nopa
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re


class staion:
    station_name :str
    time_to_NIHONBASHI :int
    transit_count_to_NIHONBASHI :int

    def __init__(self,station_name,time_to_NIHONBASHI,transit_count_to_NIHONBASHI):
        self.station_name = station_name
        self.time_to_NIHONBASHI = time_to_NIHONBASHI
        self.transit_count_to_NIHONBASHI = transit_count_to_NIHONBASHI

    def print(self):
        print (self.station_name +" , "+self.time_to_NIHONBASHI+" , "+self.transit_count_to_NIHONBASHI)


class stations:
    station_list :list[staion]
    num : int

    def __init__(self):
        self.station_list=[] 
        self.num=0

    def append(station_tmp):
        self.station_list.append(station_tmp)

    def print_all(self):
        for staion in self.station_list:
            staion.print()            
                    

driver = webdriver.Chrome()
print('connectiong to remote browser...')

min=0
url=' https://realestate.navitime.co.jp/chintai/reachable?node=00004341&lower_term='+str(min)+'&higher_term='+str(min+10)+'&transit_limit=0#/'

driver.get(url)
time.sleep(3)

station_list_item_elements = driver.find_elements(By.CLASS_NAME,"station-info-area")
stations_tmp = stations()

for station_element in station_list_item_elements:
    station_tmp=staion(
        station_element.find_element(By.CLASS_NAME,"station-name").text,
        re.findall('(.*)分',station_element.find_element(By.CLASS_NAME,"time").text)[0],
        re.findall('乗換(.*)回',station_element.find_element(By.CLASS_NAME,"transit-count").text)[0]
    )
    stations_tmp.append(station_tmp)

stations_tmp.print_all()

# ブラウザを終了する
driver.quit()
