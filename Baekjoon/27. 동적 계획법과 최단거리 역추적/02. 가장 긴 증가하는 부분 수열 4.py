"""14002 가장 긴 증가하는 부분 수열 4 / O(n^2)까지 가능"""


def LIS(num, numbers):
    """LIS 가장 긴 증가하는 부분 수열의 길이와 수열을 구하는 함수

    Args:
        num (int): 수열의 길이
        numbers (list): 주어진 수열

    Returns:
        length (int): LIS의 길이
        dp[idx] (list): LIS
    """
    dp = [[] for _ in range(num)]
    dp[0].append(numbers[0])  # 시작은 자기 자신만 들어갈 수 있다
    length = 1  # 그때 길이는 1
    idx = 0  # 위치는 0

    for i in range(num):
        for j in range(i):
            # j를 사용하여 만든 LIS에다 numbers[i]를 붙이는 것이 기존보다 길면서 LIS의 특성도 만족하면 바꿔준다
            if len(dp[i]) < len(dp[j]) + 1 and dp[j][-1] < numbers[i]:
                dp[i] = dp[j] + [numbers[i]]

        if not dp[i]:  # 만약 LIS를 생성하지 못했다면 본인만 집어넣어 길이 1에 LIS를 만든다
            dp[i].append(numbers[i])

        if len(dp[i]) > length:  # 기존의 LIS보다 더 길게 만들었다면 length와 idx를 바꿔준다
            length = len(dp[i])
            idx = i

    return length, dp[idx]


num = int(input())
numbers = list(map(int, input().split()))
length, lis = LIS(num, numbers)
print(length)
print(*lis)
