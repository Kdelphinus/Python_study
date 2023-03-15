import sys

INPUT = sys.stdin.readline


def find_square(n: int) -> int:
    dp = [0, 1]

    for i in range(2, n + 1):
        min_value = float("inf")
        j = 1

        while j**2 <= i:
            min_value = min(min_value, dp[i - j**2])
            j += 1
        dp.append(min_value + 1)
    return dp[n]


if __name__ == "__main__":
    print(find_square(int(INPUT())))
