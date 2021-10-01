"""나의 풀이"""


def solution(triangle):
    # 밑에서부터 최댓값만 더해서 올라가는 방식
    for tri in range(len(triangle) - 2, -1, -1):
        for i in range(len(triangle[tri])):
            triangle[tri][i] += max(triangle[tri + 1][i], triangle[tri + 1][i + 1])

    return triangle[0][0]
