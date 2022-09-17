"""Summer/Winter Coding(~2018)"""
# 링크: https://inspirit941.tistory.com/158
# 사고를 좀 더 유연하게 할 것


def solution(sticker):
    # 스티커가 하나일 때
    if len(sticker) == 1:
        return sticker[0]

    # 맨 앞의 스티커를 뗄 때(즉, 마지막 스티커는 떼지 못 함)
    dp = [0] * len(sticker)  # 현재 위치에서 얻을 수 있는 최대 점수
    dp[0] = sticker[0]
    dp[1] = sticker[0]
    for i in range(2, len(sticker) - 1):
        dp[i] = max(sticker[i] + dp[i - 2], dp[i - 1])

    answer = max(dp)

    # 맨 뒤의 스티커를 뗄 때(즉, 맨 앞의 스티커는 떼지 못 함)
    dp[0] = 0
    dp[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp[i] = max(sticker[i] + dp[i - 2], dp[i - 1])

    return max(max(dp), answer)


# ---------------------------------------------------------------------------------------

"""95.5점 (정확성 33개 중 3개 실패)"""


def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)

    dp = [0] * len(sticker)  # 현재 위치 스티커를 뗄 때, 최댓값
    check = [0] * len(sticker)  # 첫 번째 스티커를 뗸 여부

    dp[0] = sticker[0]
    dp[1] = sticker[1]
    dp[2] = sticker[2] + dp[0]
    check[0] = 1
    check[2] = 1

    for i in range(3, len(sticker)):
        if dp[i - 2] > dp[i - 3]:
            dp[i] = sticker[i] + dp[i - 2]
            check[i] = check[i - 2]
        else:
            dp[i] = sticker[i] + dp[i - 3]
            check[i] = check[i - 3]

    if check[-1] == 1:
        dp[-1] -= dp[0]

    return max(dp)
