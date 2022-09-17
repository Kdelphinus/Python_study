import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

"""실제 웹 페이지에서 웹 크롤링을 막아놓은 것으로 추정, 웹 크롤링 방법은 맞음"""

# 빈 리스트 생성
records = []

# 시작 페이지 지정
page_num = 1

while True:
    # HTML 코드 받아오기
    response = requests.get(
        "http://www.ssg.com/search.ssg?target=all&query=nintendo&page={}".format(
            page_num
        )
    )

    # BeautifulSoup 타입으로 변형하기
    soup = BeautifulSoup(response.text, "html.parser")

    # "prodName" 클래스가 있을 때만 상품 정보 가져오기
    if len(soup.select(".csrch_tip")) == 0:
        product_names = soup.select(
            ".cunit_info > div.cunit_md.notranslate > div > a > em.tx_ko"
        )
        product_prices = soup.select(
            ".cunit_info > div.cunit_price.notranslate > div.opt_price > em"
        )
        product_urls = soup.select(".cunit_prod > div.thmb > a > img")
        print("{}번 째 페이지 저장 중".format(page_num))
        print(".csrch_tip 개수: {}".format(len(soup.select(".csrch_tip"))))
        page_num += 1
        time.sleep(3)

        # 상품의 정보를 하나의 레코드로 만들고, 리스트에 순서대로 추가하기
        for i in range(len(product_names)):
            record = []
            record.append(product_names[i].text)
            record.append(product_prices[i].text.strip())
            record.append("https://www.ssg.com" + product_urls[i].get("src"))
            records.append(record)
    else:
        break

# DataFrame 만들기
df = pd.DataFrame(data=records, columns=["이름", "가격", "이미지 주소"])

# DataFrame 출력
print(df.head())