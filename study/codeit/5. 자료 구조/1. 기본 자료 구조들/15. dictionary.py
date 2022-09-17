# 딕셔너리는 중괄호를 사용
grades = {}

# key - value 데이터 삽입
grades["현승"] = 80
grades["태호"] = 60
grades["영훈"] = 90
grades["지웅"] = 70
grades["동욱"] = 96

print(grades)

# 한 key에 여러 value 저장 시도
grades["태호"] = 100  # value가 바뀐다

print(grades)

# key를 이용해서 value 탐색
print(grades["동욱"])
print(grades["현승"])

# key를 이용한 삭제
grades.pop("태호")
grades.pop("지웅")

print(grades)