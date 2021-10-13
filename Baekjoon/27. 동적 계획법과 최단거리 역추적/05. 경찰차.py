"""2618 경찰차"""
# 답안: https://www.acmicpc.net/source/3602611


def get_dist(i, j, accidents):
    x1, y1 = accidents[i]
    x2, y2 = accidents[j]
    return abs(x1 - x2) + abs(y1 - y2)


def build_shortest_dp(accidents, accident_num):
    dp = [[-1] * accident_num for _ in range(accident_num)]
    cars = [[-1] * accident_num for _ in range(accident_num)]

    for start in range(len(dp)):
        dp[start][-1] = 0
    for last in range(len(dp[0]) - 2, -1, -1):
        for start in range(last):
            # 현재 위치에서 직전 사건으로 가는 거리 + 직전 사건에서 현재 사건으로 가는 거리
            from_start = get_dist(start, last + 1, accidents) + dp[last][last + 1]

            # 현재 위치에서 현재 사건으로 가는 거리 + 현재 사건에서 직전 사건으로 가는 거리
            from_j = get_dist(last, last + 1, accidents) + dp[start][last + 1]

            if from_start < from_j:
                dp[start][last] = from_start
                cars[start][last] = start
            else:
                dp[start][last] = from_j
                cars[start][last] = last

    return dp, cars


def print_cars(cars):
    i = 0
    j = 1
    ret = [1, 2]
    while j < len(cars) - 1:
        if cars[i][j] == i:
            ret.append(ret[i])
            i = j
        elif cars[i][j] == j:
            ret.append(ret[j])
        j = j + 1

    for i in range(2, len(ret)):
        print(ret[i])


N = int(input())  # 도로의 개수
W = int(input())  # 처리해야 하는 사건의 개수
accidents = []
for i in range(W):
    accidents.append(tuple(map(int, input().split())))

# 경찰차의 시작 위치 추가
accidents.insert(0, (N, N))
accidents.insert(0, (1, 1))

dp, cars = build_shortest_dp(accidents, W + 2)
print(dp[0][1])
print_cars(cars)
