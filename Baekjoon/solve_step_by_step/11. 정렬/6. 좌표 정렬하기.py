"""11650 좌표 정렬하기"""

# 숫자를 받는다
n = int(input())

# 좌표를 담을 리스트
temps = []

# 좌표를 받아 리스트에 넣는다
for _ in range(n):
    temps.append(list(map(int, input().split())))

# x 좌표를 우선, y 좌표를 그 다음으로 하여 정렬한다
temps = sorted(temps, key=lambda x: (x[0], x[1]))

for i, j in temps:
    print(i, j)