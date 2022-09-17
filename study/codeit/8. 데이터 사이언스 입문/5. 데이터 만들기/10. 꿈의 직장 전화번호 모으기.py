import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/orangebottle/index")
soup = BeautifulSoup(response.text, "html.parser")

# "phoneNum" 클래스를 가진 태그 선택
phoneNum_tags = soup.select(".phoneNum")

# 빈 리스트 생성
phone_numbers = []

# 텍스트 추출해서 리스트에 담기
for tag in phoneNum_tags:
    phone_numbers.append(tag.text.strip())

# 결과 출력
print(phone_numbers)