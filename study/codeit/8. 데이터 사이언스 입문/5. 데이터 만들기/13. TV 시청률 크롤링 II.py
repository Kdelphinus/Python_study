import requests
from bs4 import BeautifulSoup

# 페이지를 담을 리스트 생성
rating_pages = []

# header 생성
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
}

years = list(range(2010, 2019))
months = list(range(1, 13))
weeks = list(range(0, 5))

for year in years:
    for month in months:
        for week in weeks:
            response = requests.get(
                "https://workey.codeit.kr/ratings/index?year="
                + str(year)
                + "&month="
                + str(month)
                + "&weekIndex="
                + str(week),
                headers=headers,
            )
            soup = BeautifulSoup(response.text, "html.parser")
            if len(soup.select(".row")) > 1:
                rating_pages.append(response.text)

# 테스트 코드
print(len(rating_pages))  # 가져온 총 페이지 수
print(rating_pages[0])  # 첫 번째 페이지의 HTML 코드
