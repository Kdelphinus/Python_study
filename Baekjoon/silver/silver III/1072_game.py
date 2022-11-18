import sys

INF = float("inf")
INPUT = sys.stdin.readline


def bs(total: int, win: int, win_rate: int) -> int:
    ans = INF
    l, r = 1, x

    while l <= r:
        mid = (l + r) // 2
        curr_rate = (win + mid) * 100 // (total + mid)

        if curr_rate > win_rate:
            ans = min(ans, mid)
            r = mid - 1
        else:
            l = mid + 1

    return ans if ans < INF else -1


if __name__ == "__main__":
    x, y = map(int, INPUT().split())
    print(bs(x, y, y * 100 // x))
