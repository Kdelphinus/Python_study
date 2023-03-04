"""
A(n) = A(n - 1) + A(n - 2) + A(n - 3)

- A(n-1), 즉 n-1을 만드는 모든 경우 + 1
- A(n-2), 즉 n-2를 만드는 모든 경우 + 2
- A(n-3), 즉 n-3을 만드는 모든 경우 + 3
"""


def dp_init():
    dp = [0, 1, 2, 4]
    for _ in range(7):
        dp.append(dp[-1] + dp[-2] + dp[-3])
    return dp


def main():
    dp = dp_init()
    t = int(input())
    for _ in range(t):
        print(dp[int(input())])


if __name__ == "__main__":
    main()
