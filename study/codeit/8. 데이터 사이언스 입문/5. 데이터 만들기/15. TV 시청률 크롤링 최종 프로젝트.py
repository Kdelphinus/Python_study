import pandas as pd
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
                period = soup.select("#weekSelectBox > option")
                rank = soup.select(".rank")
                chanel = soup.select(".channel")
                program = soup.select(".program")
                rating = soup.select(".percent")

                # 확인용
                # print(f"len(rank): {len(rank)}")
                # print(f"period : {period}")
                # print(f"period[week] : {period[week]}")
                # print(f"week : {week}")
                # print(f"rank : {rank}")
                # print(f"chanel : {chanel}")
                # print(f"program : {program}")
                # print(f"rating : {rating}")

                for i in range(1, len(rank)):
                    record = []
                    record.append(period[week].text.strip())
                    record.append(rank[i].text.strip())
                    record.append(chanel[i].text.strip())
                    record.append(program[i].text.strip())
                    record.append(rating[i].text.strip())
                    rating_pages.append(record)

                    # 확인용
                    # print(rating_pages[i - 1])
# 결과 출력
df = pd.DataFrame(
    data=rating_pages, columns=["period", "rank", "channel", "program", "rating"]
)
print(df.head(15))


"""모범답안"""
# import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# # 기간 지정
# years = list(range(2010, 2019))
# months = list(range(1, 13))
# weeks = list(range(0, 5))

# # 페이지를 담는 빈 리스트 생성
# rating_pages = []

# for year in years:
#     for month in months:
#         for week in weeks:
#             # HTML 코드 받아오기
#             response = requests.get("https://workey.codeit.kr/ratings/index?year=" + str(year) + "&month=" + str(month) + "&weekIndex=" + str(week))

#             # BeautifulSoup 타입으로 변환하기
#             soup = BeautifulSoup(response.text, 'html.parser')

#             # "row" 클래스가 1개를 넘는 경우만 페이지를 리스트에 추가
#             if len(soup.select('.row')) > 1:
#                 rating_pages.append(soup)

# # 레코드를 담는 빈 리스트 만들기
# records = []

# # 각 페이지 파싱해서 정보 얻기
# for page in rating_pages:
#     date = page.select('option[selected=selected]')[2].text
#     ranks = page.select('.row .rank')[1:]
#     channels = page.select('.row .channel')[1:]
#     programs = page.select('.row .program')[1:]
#     percents = page.select('.row .percent')[1:]

#     # 페이지에 있는 10개의 레코드를 리스트에 추가
#     for i in range(10):
#         record = []
#         record.append(date)
#         record.append(ranks[i].text)
#         record.append(channels[i].text)
#         record.append(programs[i].text)
#         record.append(percents[i].text)
#         records.append(record)

# # DataFrame 만들기
# df = pd.DataFrame(data=records, columns=['period', 'rank', 'channel', 'program', 'rating'])

# # 결과 출력
# df.head()