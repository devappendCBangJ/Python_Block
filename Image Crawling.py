# ==============================================================
# 0. 라이브러리 불러오기
# ==============================================================
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import random as rand

opener = urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

# ==============================================================
# 1. 함수 정의
# ==============================================================
# 1) 이미지 저장할 폴더 만들기
def CreateDir(dir_name):
    try:
        if not os.path.exists("./user_data"):
            os.mkdir("./user_data")

        # 키워드 폴더 만들기
        if not os.path.exists("./user_data/{}".format(dir_name)):
            os.mkdir("./user_data/{}".format(dir_name))
    except OSError:
        print("[Error] 파일 생성 실패")  # 확인용 코드

# 1) 이미지 크롤링
def Crawling_Img(target):
    print("ㅡㅡㅡ{} 이미지 검색 시작ㅡㅡㅡ".format(target))  # 확인용 코드
    # Driver로 브라우저 열기
    service = Service(executable_path=r'./chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    browser = webdriver.Chrome(service=service, options=options)

    # Driver 구글 검색창에 검색어 입력
    browser.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    search_bar = browser.find_element(By.NAME, "q")  # 구글 검색창 선택
    search_bar.send_keys(target)  # 검색어 입력
    search_bar.send_keys(Keys.RETURN)  # Enter

    Scroll_stop_time = 1
    Img_stop_time = 2

    # 스크롤 끝까지 내려주기
    last_height = browser.execute_script("return document.body.scrollHeight")  # 브라우저의 높이 탐색 by 자바스크립트
    while True:
        # 스크롤 끝까지 내려주기
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 스크롤 끝까지 내려주기
        time.sleep(Scroll_stop_time)  # 대기

        # 스크롤 끝까지 내린경우 더보기 누르기
        new_height = browser.execute_script("return document.body.scrollHeight")  # 브라우저 높이 최신화
        if new_height == last_height:
            try:
                browser.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height
    # browser.find_element_by_css_selector("html").send_keys(Keys.END)
    # time.sleep(scroll_stop_time) # 대기
    # browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN)
    # time.sleep(scroll_stop_time) # 대기

    # 폴더 생성
    CreateDir(target)

    # 이미지 크롤링
    imgs = browser.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
    count = 1
    print("ㅡㅡㅡ{} 이미지 크롤링 시작ㅡㅡㅡ".format(target))  # 확인용 코드
    for img in imgs:
        # Img_stop_time = rand.uniform(0.6, 1.0) # 테스트용 코드
        try:
            # 이미지 클릭
            browser.execute_script("arguments[0].click();", img)
            time.sleep(Img_stop_time)  # 대기

            # img_url 불러오기 -> 특정 파일명으로 저장
            img_url = browser.find_element(By.XPATH, '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]').get_attribute('src')
            if img_url not in img_set:
                img_set.add(img_url)
                path = "./user_data/" + target + "/"
                urllib.request.urlretrieve(img_url, path + img_url + ".jpg")

                print("Image saved: {}{}.jpg".format(target, count))  # 확인용 코드
                count = count + 1
            else:
                print(f"Image Overlapped: {img_url}")

            if count >= 200:
                print("[Except] {} count 초과로 인한 break !!!".format(count))  # 확인용 코드
                break
        except:
            print("[Except] 이미지 저장 실패로 인한 pass !!!")  # 확인용 코드
            pass

        # break # 테스트용

    # # 이미지 크롤링
    # img = browser.find_element_by_css_selector("div.bRMDJf.islir img")
    # cnt = 0
    # while True:
    #     try:
    #         print("●", cnt)
    #     except:
    #         print("크롤링 종료")
    #         break
    #     cnt += 1
    #     # 스크롤을 내리면 100개의 추가 이미지 등장 but 로딩 시간이 길어지면 100개의 새로운 이미지 모두를 출력하지 못할 수도 있으므로 80개씩만 더 로딩되도 END키를 누르도록 설정
    #     if cnt % 80 == 0:
    #         browser.find_element_by_css_selector("html").send_keys(Keys.END)
    #         time.sleep(3)
    #         img = browser.find_element_by_css_selector("div.bRMDJf.islir img")

    browser.close()

# ==============================================================
# 1. 변수 정의
# ==============================================================
img_set = set()

# ==============================================================
# 2. Main문 : 원하는 데이터 크롤링
# ==============================================================
targets = ["golf ball in water", "golf ball in rough", "golf ball in pond", "golf ball in sand", "golf ball in sand bunker", "golf ball in bunker", "golf ball on grass"]
for target in targets:
    try:
        Crawling_Img(target)
    except:
        print("[Except] Appcheck 랜섬웨어 오류로 인한 pass !!!")  # 확인용 코드
        pass
