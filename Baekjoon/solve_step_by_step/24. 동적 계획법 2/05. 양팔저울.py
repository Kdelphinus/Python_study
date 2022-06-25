"""2629 양팔저울"""
"""
- 양쪽 저울에 올라간 추 무게의 차이가 우리가 알 수 있는 구슬의 무게이다
- 추를 왼쪽에, 오른쪽에, 그리고 올리지 않는 가능성을 찾는 방향으로 푼 방식
- 현재 놓아야 하는 추와 현재 무게 차이를 이용해 반복적 계산을 막는 방식
- 해설: https://source-sc.tistory.com/3
"""

import sys

input = sys.stdin.readline


def double_armed_scale(weights, now, left, right, possible):
    """double_armed_scale

    Args:
        weights (list): 추가 들어있는 리스트
        now (int): 현재 올릴 추의 인덱스
        left (int): 현재 왼쪽에 올라간 추들의 무게
        right (int): 현재 오른쪽에 올라간 추들의 무게
        possible (list): 두 저울 사이의 차를 저장한 리스트
        new (int): 현재 양쪽 저울 사이의 차
    """
    new = abs(left - right)

    if new not in possible:  # 현재 추의 차이가 구한 적이 없을 때
        possible.append(new)
    if now == len(weights):  # 모든 추를 다 확인했을 때
        return
    if dp[now][new] == 0:
        # 왼쪽에 추를 두었을 때
        double_armed_scale(weights, now + 1, left + weights[now], right, possible)

        # 오른쪽에 추를 두었을 때
        double_armed_scale(weights, now + 1, left, right + weights[now], possible)

        # 추를 두지 않았을 때
        double_armed_scale(weights, now + 1, left, right, possible)

        dp[now][new] = 1


weights_num = int(input())
weights = list(map(int, input().split()))

marble_num = int(input())
marbles = list(map(int, input().split()))

# dp[now][new]: now번째 추를 사용해야 할 때, 현재 양쪽의 차이는 new이다
# 세로는 추의 개수, 가로는 나올 수 있는 차이만큼 인덱스가 필요하다
dp = [[0] * sum(weights) for _ in range(len(weights))]
possible = []

double_armed_scale(weights, 0, 0, 0, possible)

for marble in marbles:
    if marble in possible:
        print("Y", end=" ")
    else:
        print("N", end=" ")
