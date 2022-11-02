# 101
# True와 False는 bool 타입

# 102
# print(3 == 5)
# False

# 103
# print(3 < 5)
# True

# 104
# x = 4
# print(1 < x < 5)
# True

# 105
# print((3 == 3) and (4 != 3))
# True

# 106
# print(3 => 4)
# print(3 >= 4) # 부호의 순서

# 107
# if 4 < 3:
#     print("Hello World.")
# False 값이므로 아무것도 출력 안됨

# 108
# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")
# False 값이므로 "Hi, there."이 출력

# 109
# if True:
#     print("1")
#     print("2")
# else:
#     print("3")
# print("4")
# 1,2,4가 출력

# 110
# if True:
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else:
#     print("4")
# print("5")
# 3, 5가 출력

# 111
# print(input()*2)

# 112
# num = input("숫자를 입력하세요: ")
# print(10 + int(num))

# 113
# num = int(input("숫자를 입력하세요: "))
# if num % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# 114
# num = int(input("숫자를 입력하세요: ")) + 20
# if num <= 255:
#     print(num)
# else:
#     print(255)

# 115
# num = int(input("숫자를 입력하세요: ")) - 20
# if num < 0:
#     print(0)
# else:
#     print(num)

# 116
# time = input("시간을 입력하세요(hh:mm): ")
# min = int(time[3:])
# if min == 0:
#     print("정각입니다.")
# else:
#     print("정각이 아닙니다.")

# 117
# fruit = ["사과", "포도", "홍시"]
# anwser = input("좋아하는 과일은? ")
# if anwser in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# 118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# anwser = input("투자 종목을 입력하세요: ")
# if anwser in warn_investment_list:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")

# 119 딕셔너리 값 비교
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# season = input("제가 좋아하는 계절은: ")
# if season in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# 120 딕셔너리 값 비교
# anwser = input("좋아하는 과일은: ")
# if anwser in fruit.values():
#     print("정답입니다.")
# else: 
#     print("오답입니다.")

# 121
# word = input("문지 하나를 입력하시오: ")
# if word.islower == True :
#     print(word.upper())
# else:
#     print(word.lower())

# 122
# score = int(input("점수를 입력하시오: "))
# if score > 100 or score < 0:
#     print("잘못된 값입니다. 다시 입력하세요")
# elif 100 >= score > 80:
#     print("grade is A")
# elif score > 60:
#     print("grade is B")
# elif score > 40:
#     print("grade is C")
# elif score > 20:
#     print("grade is D")
# else:
#     print("grade is E")

# 123
# 환율 = {"달러" : 1167, "엔" : 1.096, "유로" : 1268, "위안" : 171}
# money = input("입력(금액,통화명): ")
# num, currency = money.split(",")
# print(float(num) * 환율[currency],  "원")

# 124
# num1 = int(input("num1: "))
# num2 = int(input("num2: "))
# num3 = int(input("num3: "))

# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num3 and num2 > num1:
#     print(num2)
# elif num3 > num1 and num3 > num2:
#     print(num3)
# elif num1 == num2 and num1 != num3:
#     print(num1, "(num1 = num2)")
# elif num1 == num3 and num1 != num2:
#     print(num1, "(num1 = num3)")
# elif num2 == num3 and num2 != num1:
#     print(num2, "(num2 = num3)")
# else:
#     print(num1, "(num1 = num2 = num3)")

# 125
# phone = {"011":"SKT", "016":"KT", "019":"LGU"}
# num = input("휴대전화 번호 입력: ")
# if num[0:3] in phone:
#     print("당신은", phone[num[0:3]], "사용자입니다.")
# elif num[0:3] == "010":
#     print("당신의 통신사를 알 수 없습니다.")
# else:
#     print("잘못된 번호입니다.")

# 126
# post = {"010":"강북구", "011":"강북구", "012":"강북구",
#     "013":"도봉구", "014":"도봉구", "015":"도봉구",
#     "016":"노원구","017":"노원구", "018":"노원구", "019":"노원구"}
# user = input("우편번호 5자리를 입력하세요: ")
# if len(user) == 5:
#     if user[0:3] in post:
#         print(post[user[0:3]])
#     else:
#         print("없는 우편번호입니다.")
# else:
#     print("잘못된 값입니다. 5자리를 입력하세요.")

# 127, 128, 129
# num = str(input("주민등록번호: "))
# check = (11 - (((int(num[0]) + int(num[9])) * 2 + (int(num[1]) + int(num[10])) * 3 \
#     + (int(num[2]) + int(num[11])) * 4 + (int(num[3]) + int(num[12])) * 5 \
#     + int(num[4]) * 6 + int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9) % 11)) \
#     == int(num[13])

# if len(num) == 14:
#     if check == True:
#         if num[7] == "1" or num[7] == "3":
#             print("남")
#         else:
#             print("여")

#         if 0 <= int(num[8:10]) <= 8:
#             print("서울 출신입니다.")
#         elif 9 <= int(num[8:10]) <= 12:
#             print("부산 출신입니다.")
#         else:
#             print("서울, 부산 출신이 아닙니다.")
#     else:
#         print("유효하지 않은 주민등록번호입니다.")
# else:
#     print("잘못된 값입니다. '-'을 포함하여 14자리를 입력하세요.")