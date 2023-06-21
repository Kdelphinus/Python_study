# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됨

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20으로 가정
# 조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈과 shuffle과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# from random import *
# lst = [1,2,3,4,5]
# # print(lst)
# # shuffle(lst)
# # print(lst)
# print(sample(lst, 1))

from random import *

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(lst)
chiken = sample(lst, 1)
# print(chiken)
coffee = sample(lst, 3)
# print(coffee)

# 따로 뽑으면 중복 가능성이 있음

print(f"-- 당첨자 발표 --\n치킨 당첨자 : {chiken}\n커피 당첨자 : {coffee}\n-- 축하합니다 --")

# 모범 답안

users = range(1, 21)  # 1부터 20까지의 숫자를 생성
# print(type(users)) # range 타입임
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)  # 1명은 치킨, 3명은 커피
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")
