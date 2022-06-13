# 크롬드라이버 다운받고 경로 바꿔줘야 함

import time

from selenium import webdriver
import requests


# 웹드라이버 생성
driver = webdriver.Chrome('/Users/jho/Desktop/chromedriver')
driver.implicitly_wait(3)


# https://workey.codeit.kr/costagram 접속
time.sleep(1)
driver.get('https://workey.codeit.kr/costagram')


# 로그인 버튼 클릭
time.sleep(1.5)
driver.find_element_by_class_name('top-nav__login-link').click()
# ID 입력
time.sleep(1.5)
driver.find_element_by_class_name('login-container__login-input').send_keys('codeit')
# 비밀번호 입력
time.sleep(1.5)
driver.find_element_by_class_name('login-container__password-input').send_keys('datascience')
# 로그인
time.sleep(1.5)
driver.find_element_by_class_name('login-container__login-button').click()


# 웹 페이지 가장 밑으로 스크롤
# scrollHeight 가져오기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrollHeight 까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # scrollHeight 비교
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


# 이미지 다운로드
for elt in driver.find_elements_by_class_name('post-list__post.post'):
    # 'style'이라는 속성에서 이미지 url (이미지 주소) 추출
    style_string = elt.get_attribute('style')
    img_url = 'https://workey.codeit.kr' + style_string.split(' url("')[1].split('")')[0]
    # 이미지 저장할 경로 정의
    img_path = '/Users/jho/Desktop/my_images/' + img_url.split('/')[-1]
    # requests 패키지 써서 이미지 다운로드
    response = requests.get(img_url)
    if response.status_code == 200:
        with open(img_path, 'wb+') as f:
            f.write(response.content)

