"""1780 종이의 개수"""
import sys

input = sys.stdin.readline
minus_one, zero, one = 0, 0, 0  # -1 종이의 수, 0 종이의 수, 1 종이의 수


def oneColor(n, y, x):
    global minus_one, zero, one

    if n == 1:  # 종이의 크기가 1칸일 때
        if papers[y][x] == "-1":
            minus_one += 1
        elif papers[y][x] == "0":
            zero += 1
        else:
            one += 1
        return

    flag = True  # 현재 종이가 같은 숫자인지 확인
    for j in range(y, y + n):
        if not flag:
            break
        for i in range(x, x + n):
            if papers[y][x] != papers[j][i]:
                flag = False
                break

    if flag:  # 다 같은 숫자일 때
        if papers[y][x] == "-1":
            minus_one += 1
        elif papers[y][x] == "0":
            zero += 1
        else:
            one += 1
        return
    else:  # 다른 숫자일 때
        n //= 3
        # 윗 줄
        oneColor(n, y, x)
        oneColor(n, y, x + n)
        oneColor(n, y, x + n * 2)
        # 중간 줄
        oneColor(n, y + n, x)
        oneColor(n, y + n, x + n)
        oneColor(n, y + n, x + n * 2)
        # 아랫 줄
        oneColor(n, y + n * 2, x)
        oneColor(n, y + n * 2, x + n)
        oneColor(n, y + n * 2, x + n * 2)


num = int(input().rstrip())  # 3의 제곱승으로만 들어옴
papers = [list(input().split()) for _ in range(num)]  # 종이의 상태를 받음
oneColor(num, 0, 0)
print(minus_one)
print(zero)
print(one)