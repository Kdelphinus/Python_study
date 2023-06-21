num = int(input())

for i in range(1, num + 1):
    cnt = 0
    temp = i
    while temp > 0:  # 숫자에 들어있는 3, 6, 9 숫자를 셈
        if temp % 10 == 3 or temp % 10 == 6 or temp % 10 == 9:
            cnt += 1
        temp //= 10

    if cnt == 0:  # 없으면 숫자 출력
        print(i, end=" ")
    else:  # 있으면 개수만큼 - 출력
        for _ in range(cnt):
            print("-", end="")
        print(" ", end="")
