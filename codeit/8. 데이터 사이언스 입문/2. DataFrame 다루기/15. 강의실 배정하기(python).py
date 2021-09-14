import pandas as pd

# 파일 불러오기
df = pd.read_csv("data/codeit/enrolment.csv")


"""수강 가능 강의와 불가능한 강의 나누기"""
# status column을 생성
df["status"] = "allowed"

# 1학년과 4학년이 못 듣는 과목 조건
one_grade = (df["course name"] == "information technology") & (df["year"] == 1)
four_grade = (df["course name"] == "commerce") & (df["year"] == 4)

df.loc[one_grade | four_grade, "status"] = "not allowed"  # 두 조건 중 하나만 해당되도 듣지 못함

# 과목별 수강 인원
allowed = df["status"] == "allowed"  # 1, 4학년 조건에 해당하지 않는 인원들
count = df.loc[allowed, "course name"].value_counts()
cloesed_class = list(count[count < 5].index)
# 수강인원 미달인 강의는 듣지 못함
for course in cloesed_class:
    df.loc[df["course name"] == course, "status"] = "not allowed"


"""강의실 배정하기 - 규모별로 분류"""
# room assignment column 생성
df["room assignment"] = "not assignment"

allowed = df["status"] == "allowed"
count = df.loc[allowed, "course name"].value_counts()

# 강의실 배정 조건
auditorium = list(count[count >= 80].index)
large_room = list(count[(count >= 40) & (count < 80)].index)
medium_room = list(count[(count >= 15) & (count < 40)].index)
small_room = list(count[(count >= 5) & (count < 15)].index)

# 강의실 배정
for course in auditorium:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Auditorium"
for course in large_room:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Large room"
for course in medium_room:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Medium room"
for course in small_room:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Small room"


"""강의실 배정하기 - 구체적으로 배정"""
"""절차를 하나씩 보기 위해서 위의 코드와 중복되는 것이 있음"""
# 강의실 번호 배정
for i in range(len(auditorium)):
    df.loc[
        (df["course name"] == sorted(auditorium)[i]) & allowed, "room assignment"
    ] = "Auditorium-{}".format(i + 1)
for i in range(len(large_room)):
    df.loc[
        (df["course name"] == sorted(large_room)[i]) & allowed, "room assignment"
    ] = "Large-{}".format(i + 1)
for i in range(len(medium_room)):
    df.loc[
        (df["course name"] == sorted(medium_room)[i]) & allowed, "room assignment"
    ] = "Medium-{}".format(i + 1)
for i in range(len(small_room)):
    df.loc[
        (df["course name"] == sorted(small_room)[i]) & allowed, "room assignment"
    ] = "Small-{}".format(i + 1)

# column 이름 바꾸기
df.rename(columns={"room assignment": "room number"}, inplace=True)

print(df)
