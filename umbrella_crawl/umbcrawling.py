import os
import sys

import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

from tensorflow_datasets.object_detection.open_images_challenge2019_beam import cv2


class Model(object):
    def crawling(self):
        search = "우산"   # 이미지 이름
        count = 101    # 크롤링할 이미지 개수
        saveurl = r"C:\Users\seongbae\Desktop\borrow_sub\umbrella_crawl\save\umb"  # 이미지들을 저장할 폴더 주소

        ## 셀레니움으로 구글 이미지 접속 후 이미지 검색

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

                try:
                    driver.find_element_by_css_selector(".mye4qd").click()

                except:
                    break

            last_height = new_height

        #이미지 찾고 다운받기
        images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

        for i in range(count):

            try:
                images[i].click() # 이미지 클릭
                time.sleep(1)

                imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")

                src = cv2.imread(imgUrl, cv2.IMREAD_GRAYSCALE)

                if src is None:
                    print('Image load failed!')
                    sys.exit()
                edges = cv2.Canny(src, 50, 150)
                lines = cv2.HoughLinesP(edges, 1.0, np.pi / 180, 160, minLineLength=50, maxLineGap=5)
                dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

                if lines is not None:
                    for i in range(lines.shape[0]):  # range(N)
                        pt1 = (lines[i][0][0], lines[i][0][1])
                        pt2 = (lines[i][0][2], lines[i][0][3])
                        cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

                urllib.request.urlretrieve(imgUrl, saveurl + str(i) + ".jpg")    # 이미지 다운
                cv2.waitKey()
            except:
                pass
        driver.close()

if __name__ == '__main__':
    Model().crawling()