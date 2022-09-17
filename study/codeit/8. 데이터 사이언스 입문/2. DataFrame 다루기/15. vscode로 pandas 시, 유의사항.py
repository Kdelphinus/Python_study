import pandas as pd

"""
현재 작업 폴더는 python으로 지정되어 있다.
그렇기에 python 폴더를 기준으로 경로를 지정해주어야 한다
"""

samsong_df = pd.read_csv("codeit/8. 데이터 사이언스 입문/4. DataFrame 다루기/data/samsong.csv")
hyundee_df = pd.read_csv("codeit/8. 데이터 사이언스 입문/4. DataFrame 다루기/data/hyundee.csv")

day = samsong_df["요일"]
samsong_culture = samsong_df["문화생활비"]
hyundee_culture = hyundee_df["문화생활비"]

dict = {"day": day, "samsong": samsong_culture, "hyundee": hyundee_culture}
df = pd.DataFrame(dict)
print(df)