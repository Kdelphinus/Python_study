# 참고: https://ku-hug.tistory.com/209


def make_dp():
    # 1로만 조합된 식은 모든 숫자가 가능
    dp = [1] * 10001

    # 1로만 조합된 식에 2를 더하는 방법 추가
    for i in range(2, 10001):
        dp[i] += dp[i - 2]

    # 1, 2로만 조합된 식에 3을 더하는 방법 추가
    for i in range(3, 10001):
        dp[i] += dp[i - 3]

    return dp


if __name__ == "__main__":
    DP = make_dp()
    T = int(input())
    for _ in range(T):
        print(DP[int(input())])
