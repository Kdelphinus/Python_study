"""2618 경찰차"""


def __distance(now, goal):
    return abs(now[0] - goal[0]) + abs(now[1] - goal[1])


def police_car(n):
    first_car = [0, 0]
    second_car = [n - 1, n - 1]

    return


n = int(input())
case_num = int(input())
cases = [list(map(int, input().split())) for _ in range(case_num)]
