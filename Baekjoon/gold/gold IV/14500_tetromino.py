# 2chanhaeng의 풀이: https://www.acmicpc.net/source/48743661
# 위 풀이로 시간 단축


import sys

input = sys.stdin.readline


def dfs(y: int, x: int, cnt: int, result: int, ans: int, maxcell: int):
    if ans >= result + maxcell * (3 - cnt):
        return ans

    if cnt == 3:
        return max(ans, result)

    for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(visit) and 0 <= nx < len(visit[0]) and not visit[ny][nx]:
            if cnt == 1:
                visit[ny][nx] = 1
                ans = dfs(y, x, cnt + 1, result + board[ny][nx], ans, maxcell)
                visit[ny][nx] = 0
            visit[ny][nx] = 1
            ans = dfs(ny, nx, cnt + 1, result + board[ny][nx], ans, maxcell)
            visit[ny][nx] = 0
    return ans


def tetromino():
    global board, visit

    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    ans = maxcell = max(map(max, board))

    for y in range(n):
        for x in range(m):
            visit[y][x] = 1
            ans = dfs(y, x, 0, board[y][x], ans, maxcell)
            visit[y][x] = 0

    return ans


if __name__ == "__main__":
    print(tetromino())