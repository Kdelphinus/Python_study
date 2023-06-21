# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5]) # 없는 값이 나오면 오류로 종료
# print(cabinet.get(5)) # 없는 값을 none으로 출력하고 작업 계속
# print(cabinet.get(5, "사용 가능"))
# print("hi")

# print(3 in cabinet) # 있으면 True, 없으면 False

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet.get("B-100"))

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# 둘 다 출력
print(cabinet.items())

# 목욕탕 마감
cabinet.clear()
print(cabinet)
