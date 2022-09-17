import requests

years = list(range(2010, 2019))
months = list(range(1, 13))
weeks = list(range(0, 5))

# 페이지들을 담을 리스트
rating_pages = []

for year in years:
    for month in months:
        for week in weeks:
            respon = requests.get(
                "https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(
                    year, month, week
                )
            )
            rating_pages.append(respon.text)

print(len(rating_pages))  # 가져온 총 페이지 수
print(rating_pages[0])  # 첫 번째 페이지의 HTML 코드
