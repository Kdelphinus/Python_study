# # # print(5)
# # # print(-10)
# # # print(3.14)
# # # print(1000)
# # # print(5+3)
# # # print(2*8)
# # # print(3*(3+1))
# # # print('풍선')
# # # print("나비")
# # # print("ㅋ"*9)
# # # # 참 / 거짓
# # # print(5>10)
# # # print(5<10)
# # # print(True)
# # # print(False)
# # # print(not True)
# # # print(not (5>10))

# # # #애완동물을 소개해 주세요~
# # # name = "연탄이"
# # # animal = "강아지"
# # # age = 4
# # # hobby = "산책"
# # # is_adult = age>=3

# # # ''' 이렇게 하면
# # # 여러 문장이
# # # 주석 처리 됩니다. '''

# # # # 혹은 ctrl +/

# # # print("우리집 " + animal +"의 이름은 " + name + "에요")
# # # hobby = "공놀이"
# # # # print(name +"는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# # # print(name,"는",age,"살이며,",hobby,"을 아주 좋아해요")
# # # print(name + "는 어른일까요? " + str(is_adult))

# # # print(2**3)
# # # print(10%3) #나머지
# # # print(10//3) #몫

# # # print(10>3) # True
# # # print(4>=7) # False

# # # print(3 == 3) # 앞 뒤과 같다는 것을 의미
# # # print(4==2)
# # # print(3+4==7)

# # # print(1 != 3) #같지 않다
# # # print(not(1 != 3))

# # # print((3>0) and (3<5)) #두 조건 모두 만족하는가
# # # print((3>0)&(3<5)) #and와 같은 의미

# # # print((3>0) or (3>5))
# # # print((3>0) | (3>5)) #or와 같은 의미

# # # print(5>4>3)
# # # print(5>4>7)

# # # #수식
# # # number = 2+3*4
# # # print(number)
# # # number = number + 2
# # # print(number)
# # # number += 2
# # # print(number)
# # # number *= 2
# # # print(number)
# # # number /= 2
# # # print(number)
# # # number -= 2
# # # print(number)

# # # number %= 2
# # # print(number)

# # # print(abs(-5)) #절댓값
# # # print(pow(4, 2)) #제곱
# # # print(max(5, 12)) #최댓값
# # # print(min(5, 12))
# # # print(round(3.14)) #반올림
# # # print(round(3.65)) 

# # from math import *
# # # print(floor(4.99)) #내림
# # # print(ceil(3.14)) #올림
# # # print(sqrt(16)) #제곱근

# # # # #랜덤함수
# # # from random import *

# # # # print(random()) #0.0 ~ 1.0 사이 임의의 값을 생성
# # # # print(random() * 10) #0.0 ~ 10.0 사이 임의의 값을 생성
# # # # print(int(random() * 10)) #int는 정수 값
# # # # print(int(random() * 10))
# # # # print(int(random() * 10))
# # # # print(int(random() * 10) + 1) #1 ~ 10 이하 임의의 값 생성

# # # # print(int(random() * 45 + 1)) #1 ~ 45 이하의 임의의 값을 생성

# # # print(randrange(1, 46)) #1 ~ 46 미만의 임의의 값을 생성
# # # print(randrange(1, 46)) #1 ~ 46 미만의 임의의 값을 생성
# # # print(randrange(1, 46)) #1 ~ 46 미만의 임의의 값을 생성
# # # print(randrange(1, 46)) #1 ~ 46 미만의 임의의 값을 생성
# # # print(randrange(1, 46)) #1 ~ 46 미만의 임의의 값을 생성
# # # print(randrange(1, 46)) #1 ~ 46 미만의 임의의 값을 생성
# # # print(randrange(1, 46)) #1 ~ 46 미만의 임의의 값을 생성

# # # print(randint(1, 45)) #1 ~ 45 이하의 임의의 값 생성

# # # #문자열
# # # sentence = '나는 소년입니다'
# # # print(sentence)
# # # sentence2 = "파이썬은 쉬어요"
# # # print(sentence2)
# # # sentence3 = """
# # # 나는 소년이고,
# # # 파이썬은 쉬어요
# # # """
# # # print(sentence3)

# # #슬래싱
# # jumin = "951015-1234567"

# # print("성별: " + jumin[7]) #0부터 시작하여 숫자를 세야함
# # print("연: " + jumin[0:2]) #시작자리부터 직전 값까지(마지막값은 출력 안됨)
# # print("월: " + jumin[2:4])
# # print("일: " + jumin[4:6])
# # print("생년월일: " + jumin[:6]) #처음부터 6직전까지
# # print("뒤 7자리: " + jumin[7:14])
# # print("뒤 7자리: " + jumin[7:])
# # print("뒤 7자리: " + jumin[-7:]) #맨 뒤가 -1로 시작하여 가져올 부분까지

# #문장

python = "Python is Amazing"
# print(python.lower()) #소문자로 변경
# print(python.upper())
# print(python[0].isupper()) #대문자가 맞는가?
# print(len(python)) #길이
# print(python.replace("Python", "Java")) #문자 바꾸기

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 두 번째 n의 위치
print(index)

# print(python.find("n")) #찾기
# print(python.find("Java")) # 찾는 값이 없으면 -1
# # print(python.index("Java")) # 찾는 값이 없으면 오류

# print(python.count("n")) # n의 등장 횟수

# 문자열

# print("a" + "b")
# print("a", "b")

# # 방법 1
# print("나는 %d 살 입니다." % 20) # 정수값
# print("나는 %s을 좋아해요" % "파이썬") # 글자값
# print("Apple은 %c로 시작해요" % "A") #c는 한 글자만 

# # %s는 어떤 것이든 잘 가져옴
# print("나는 %s 살 입니다." % 20) # 정수값

# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨강"))

# 방법 2
# print("나는 {}살 입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20))


# 방법 4
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.") # f로 시작하면 변수를 중괄호로 가져올 수 있음

# \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")

# print("저는 '고명준'입니다.")
# print('저는 "고명준"입니다.')
# print("저는 \"고명준\"입니다.") #\" : 문장 내 "" 사용가능

#\\: 문장 내에서 \
# print("C:\\Users\\delphinus\\Desktop\\PythonWorkspace>")

# \r: 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# # /b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# # /t : 탭
# print("Red\tApple")

