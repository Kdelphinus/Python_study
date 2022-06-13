import time
import requests
from bs4 import BeautifulSoup

# 빈 리스트 생성
pages = []

# 첫 페이지 번호 지정
page_num = 1

# headers 지정
# user-agent는 사용자를 대표해서 여러가지 작업을 해 주는 프로그램, 북마크 참고
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
}

while True:
    # HTML 코드 받아오기, 위에서 지정해 준 headers 설정해 주기
    response = requests.get(
        "http://www.ssg.com/search.ssg?target=all&query=nintendo&page=" + str(page_num),
        headers=headers,
    )

    # BeautifulSoup 타입으로 변환하기
    soup = BeautifulSoup(response.text, "html.parser")

    # ".csrch_tip" 클래스가 없을 때만 HTML 코드를 리스트에 담기
    # http://www.ssg.com/search.ssg?target=all&query=nintendo&page=999 를 들어가면 "검색어와 일치하는 상품이 없습니다"가 나옴
    # 상품이 있는 페이지와 없는 페이지의 차이를 찾아봐야 함
    # 쓱은 .csech_tip이 상품이 없는 페이지에만 존재
    if len(soup.select(".csrch_tip")) == 0:
        pages.append(soup)
        print(str(page_num) + "번째 페이지 가져오기 완료")
        page_num += 1

        # 크롤링을 악용하는 나쁜 봇을 차단하기 위해 방어수단을 사용하는 웹사이트들 다수 존재
        # 차단되지 않기 위해서 한 페이지 당 3초 쉰 뒤 가져오는 것으로 진행
        time.sleep(3)
    else:
        break

# 가져온 페이지 개수 출력하기
print(len(pages))