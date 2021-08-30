"""찾아라 프로그래밍 마에스터"""


def solution(maps):
    height = len(maps)
    width = len(maps[0])
    visit = [[0] * width for _ in range(height)]
    dp = [[0] * width for _ in range(height)]

    dp[0][0] = 1
    nx = [0, 0, 1, -1]
    ny = [1, -1, 0, 0]
    queue = [[0, 0]]

    while queue:
        y, x = queue[0][0], queue[0][1]
        del queue[0]

        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if 0 <= dx < width and 0 <= dy < height:
                if not visit[dy][dx] and maps[dy][dx]:
                    queue.append([dy, dx])
                    visit[dy][dx] = 1
                    dp[dy][dx] = dp[y][x] + 1

    return dp[height - 1][width - 1] if dp[height - 1][width - 1] else -1


maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
]
print(solution(maps))  # 11, 최단 거리

maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
]
print(solution(maps))  # -1, 갈 수 없음
