import numpy as np
from matplotlib import pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
from tensorflow import keras
os.environ['KMP_DUPLICATE_LIB_OK']='True'

class Crawling(object):
    def __init__(self):
        global search, count, save, img_name
        img_name = "파손_영어"
        search = "broken umbrella"
        count = 10000  # 크롤링할 이미지 개수
        save = r"C:\Users\AIA\PycharmProjects\borrow_sub\umbrella_crawl\data\broken_umb_eng"

    def image_crawling(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument("window-size=1920x1080")
        driver = webdriver.Chrome(options=options)  #options=options
        driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
        elem = driver.find_element_by_name("q")
        elem.send_keys(search)

        elem.send_keys(Keys.RETURN)

        # 페이지 끝까지 스크롤 내리기
        SCROLL_PAUSE_TIME = 1
        # 스크롤 깊이 측정하기
        last_height = driver.execute_script("return document.body.scrollHeight")

        # 스크롤 끝까지 내리기

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # 페이지 로딩 기다리기
            time.sleep(SCROLL_PAUSE_TIME)
            # 더 보기 요소 있을 경우 클릭하기

            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                driver.find_element_by_css_selector(".mye4qd").click()
            else:
                break

            last_height = new_height

        #이미지 찾고 다운받기
        images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

        for i in range(count):
            images[i].click() # 이미지 클릭
            time.sleep(10)

            imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
            urllib.request.urlretrieve(imgUrl, save + '/'+ img_name + str(i) + ".jpg")    # 이미지 다운

        driver.close()




if __name__ == '__main__':
    Crawling().image_crawling()