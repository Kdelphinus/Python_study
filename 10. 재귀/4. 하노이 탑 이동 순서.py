"""11729 하노이 탑 이동 순서"""


def count(start, end):
    global list_1
    list_1.append(f"{start} {end}")


def hanoi(num, start=1, end=3):
    if num == 0:
        return

    # 출발도 도착지도 아닌 다른 기둥
    other = 6 - end - start

    hanoi(num - 1, start, other)
    count(start, end)
    hanoi(num - 1, other, end)


# 경로를 저장할 리스트
list_1 = []

# 원판의 개수를 받는다
num = int(input())

hanoi(num)

# 옮긴 횟수 출력
print(len(list_1))

# 경로 출력
for i in list_1:
    print(i)

# ----------------------------------------------------------------------
"""다른 답안"""
n = int(input())


def hanoi_2(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi_2(n - 1, a, c, b)
        print(a, c)
        hanoi_2(n - 1, b, a, c)


sum = 1

for i in range(n - 1):
    sum = sum * 2 + 1

print(sum)
hanoi_2(n, 1, 2, 3)
