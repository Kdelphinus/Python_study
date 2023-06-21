# for

# for waiting_no in [1,2,3,4,5] :
#     print("대기번호 : {0}" .format(waiting_no))

# for waiting_no in range(5) : # 0~4까지 나옴
#     print("대기번호 : {0}" .format(waiting_no))

# for waiting_no in range(1,6) : # 1~5까지 나옴
#     print("대기번호 : {0}" .format(waiting_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다." .format(customer))


# while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요." .format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회" .format(customer, index))
#     index += 1

# 무한루프를 끝내려면 터미널에 ctrl + c를 누르면 됨

# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비 되었습니다." .format(customer))
#     person = input("이름이 어떻게 되세요? ")

# continue와 break
# absent = [2, 5] # 결석
# no_book = [7] # 책을 안 가져옴
# for student in range(1,11) : # 출석번호가 1~10까지 있음
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와" .format(student))
#         break # 반복을 끝내버림
#     print("{0}, 책을 읽어봐" .format(student))


# 한줄문 for
# 출석번호가 1, 2, 3, 4 였는데 앞에 100을 붙여 101, 102...로 변경
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iorn man", "Thor", "Groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변경
students = ["Iorn man", "Thor", "Groot"]
students = [i.upper() for i in students]
print(students)
