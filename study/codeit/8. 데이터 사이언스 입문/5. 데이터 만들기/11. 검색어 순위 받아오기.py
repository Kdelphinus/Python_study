import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/music/index")
soup = BeautifulSoup(response.text, "html.parser")

rank__order_tag = soup.select(".rank__order li")

rank__order = []

# strip()까지 하면 순위/변동순위/이름이 순서대로 다 나온다
# 이를 공백 기준으로 나눈 뒤, 가장 마지막에 있는 이름만 가져온 것
for li in rank__order_tag:
    rank__order.append(li.text.strip().split(" ")[2])

print(rank__order)
