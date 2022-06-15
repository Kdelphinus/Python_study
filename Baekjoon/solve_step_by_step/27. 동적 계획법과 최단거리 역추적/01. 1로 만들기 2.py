"""12852 1로 만들기 2"""


def make_to_one(num):
    dp = [[] for _ in range(num + 1)]  # index에서 1로 만드는 최단 과정을 저장할 리스트
    dp[1] = [1]  # 1은 1 하나로 과정 끝
    for i in range(2, num + 1):
        dp[i] = dp[i - 1] + [i]  # 1을 빼는 연산

        # 2로 나눠지고 2로 나눈 것이 기존보다 과정을 줄일 때
        if i % 2 == 0 and len(dp[i // 2]) + 1 < len(dp[i]):
            dp[i] = dp[i // 2] + [i]

        # 3으로 나눠지고 3으로 나눈 것이 기존보다 과정을 줄일 때
        if i % 3 == 0 and len(dp[i // 3]) + 1 < len(dp[i]):
            dp[i] = dp[i // 3] + [i]

    print(len(dp[num]) - 1)  # 연산 횟수, 본인은 제외한다
    print(*sorted(dp[num], reverse=True))  # 오름차순으로 저장되기에 역순으로 출력


num = int(input())
make_to_one(num)
