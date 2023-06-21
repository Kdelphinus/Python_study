"""월간 코드 챌린지 시즌 1"""


# 링크: https://developnote.tistory.com/26
def solution(n):
    anw = [[0 for j in range(1, i + 1)] for i in range(1, n + 1)]
    num = 0
    x, y = 0, -1
    for i in range(n):  # 방향 전환 횟수가 n번
        for j in range(i, n):  # 방향을 전환할 때마다 채워야 하는 수가 하나씩 줄음
            if i % 3 == 0:  # 밑으로
                y += 1
            elif i % 3 == 1:  # 오른쪽으로
                x += 1
            else:  # 위쪽으로
                y -= 1
                x -= 1
            num += 1
            anw[y][x] = num

    return sum(anw, [])


print(solution(4))  # [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]
print(solution(5))  # [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9]
