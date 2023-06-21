test = int(input())

for t in range(test):
    word = input()
    length = len(word)
    flag = True

    for i in range(length // 2):  # 앞, 뒤 문자를 확인
        if word[i] != word[-i - 1]:  # 다르면 다르다 표시하고 반복문 종료
            flag = False
            break

    print("#{}".format(t + 1), end=" ")
    if flag:
        print(1)
    else:
        print(0)
