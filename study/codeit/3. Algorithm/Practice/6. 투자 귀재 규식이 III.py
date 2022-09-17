def sublist_max(profits):
    if len(profits) == 1:
        return profits[0]

    start = 0
    end = len(profits) - 1

    max_profits = sum(profits[start : end + 1])

    return max(
        max_profits,
        sublist_max(profits[start + 1 : end + 1]),
        sublist_max(profits[start:end]),
    )


# 테스트
# print(sublist_max([7, -3, 4, -8]))
# print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))
# print(
#     sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1, -5, -9, 12, 13, -10, 5, 3, -2, -9, 5])
# )


# 해답
def sublist_max(profits):
    max_profit_so_far = profits[0]  # 반복문에서 현재까지의 부분 문제의 답
    max_check = profits[0]  # 가장 끝 요소를 포함하는 구간의 최대 합

    # 반복문을 통하여 각 요소까지의 최대 수익을 저장한다
    for i in range(1, len(profits)):
        # 새로운 요소를 포함하는 구간의 최대합을 비교를 통해 정한다
        max_check = max(max_check + profits[i], profits[i])

        # 최대 구간 합을 비교를 통해 정한다
        max_profit_so_far = max(max_profit_so_far, max_check)

    return max_profit_so_far


print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))
print(
    sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1, -5, -9, 12, 13, -10, 5, 3, -2, -9, 5])
)
