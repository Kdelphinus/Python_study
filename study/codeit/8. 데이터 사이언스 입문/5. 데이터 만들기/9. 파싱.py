import requests
from bs4 import BeautifulSoup

# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/music/index")

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(response.text, "html.parser")

# "popular__order" 클래스를 가진 태그에 중첩된 모든 <li> 태그 선택
li_tags = soup.select(".popular__order li")

# 빈 리스트 생성
popular_artists = []

# 텍스트 추출해서 리스트에 담기
for li in li_tags:
    popular_artists.append(li.text.strip())

# 결과 출력
print(popular_artists)