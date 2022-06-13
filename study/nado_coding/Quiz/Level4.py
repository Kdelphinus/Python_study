# Quiz) 행맨 게임 프로그램을 만드시오.

# - 리스트에 3개 이상의 단어 추가
# - 위 리스트에서 랜덤으로 1개의 단어를 선택
# - 단어의 길이에 맞게 밑줄 출력
# - 사용자로부터 1글자씩 입력을 받되, 단어에 입력값이 포함되면 'Correct' 출력, 아니면 "Wrong" 출력
# - 매번 입력 받을 때마다 현재까지 맞힌 글자들 표시(맞히지 못한 글자는 밑줄 출력)
# - 정답을 맞히면 Succeed 출력 후 프로그램 종료(횟수 제한 없음)

from random import *

# word = ["apple", "banana", "melon", "orange", "egg"]
# question = word[randint(0,len(word))]

# for i in question:
#     print("_" * len(question))
#     user_input = input("Input letter >")
#     if user_input == i:
#         print("Correct")

words = ["apple", "banana", "melon", "orange", "egg"]
word = choice(words)
print("answer : " + word)
letters = "" # 사용자로부터 지금까지 입력받은 모든 알파벳

while True:
    succeed = True
    print()
    for w in word:
        if w in letters:
            print(w, end = " ")
        else:
            print("_", end = " ")
            succeed = False
    print()

    if succeed:
        print("Success")
        break

    letter = input("Input letter > ")
    if letter not in letters:
        letters += letter

    if letter in word:
        print("correct")
    else:
        print("Wrong")