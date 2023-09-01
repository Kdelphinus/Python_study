def find_high_boom(n, ground, booms):
    values = [[0 for _ in range(n)] for __ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]

    for y, x in booms:
        for dy, dx in directions:
            ny, nx = y - 1 + dy, x - 1 + dx
            if 0 <= ny < n and 0 <= nx < n and ground[ny][nx] != "#":
                values[ny][nx] += 2 if ground[ny][nx] == "@" else 1

    ans = 0
    for v in values:
        ans = max(ans, max(v))

    return ans


if __name__ == "__main__":
    N, K = map(int, input().split())
    GROUND = [list(input().split()) for _ in range(N)]
    BOOMS = [tuple(map(int, input().split())) for _ in range(K)]
    print(find_high_boom(N, GROUND, BOOMS))
