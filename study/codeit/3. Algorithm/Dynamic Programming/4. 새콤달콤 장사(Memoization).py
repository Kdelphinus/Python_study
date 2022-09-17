def max_profit_memo(price_list, count, cache):
    if count <= 1:
        cache[count] = price_list[count]
        return cache[count]

    if count in cache:
        return cache[count]

    # 끝까지 구하지 못한 구간
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    for i in range(1, count // 2 + 1):
        profit = max(
            profit,
            max_profit_memo(price_list, i, cache)
            + max_profit_memo(price_list, count - i, cache),
        )
    # i의 범위를 0부터 하면 뒤의 값 count가 5가 되면서 무한루프에 빠짐

    cache[count] = profit
    return cache[count]


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))


# -----------------------------------------------------------------------------------------------------------------

# 모범답안
# def max_profit_memo(price_list, count, cache):
#     # Base Case: 0개 혹은 1개면 부분 문제로 나눌 필요가 없기 때문에 가격을 바로 리턴한다
#     if count < 2:
#         cache[count] = price_list[count]
#         return price_list[count]

#     # 이미 계산한 값이면 cache에 저장된 값을 리턴한다
#     if count in cache:
#         return cache[count]

#     # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
#     # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정
#     # 팔려고 하는 총개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
#     if count < len(price_list):
#         profit = price_list[count]
#     else:
#         profit = 0

#     # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 profit에 저장
#     for i in range(1, count // 2 + 1):
#         profit = max(profit, max_profit_memo(price_list, i, cache)
#                  + max_profit_memo(price_list, count - i, cache))

#     # 계산된 최대 수익을 cache에 저장
#     cache[count] = profit

#     return profit


# def max_profit(price_list, count):
#     max_profit_cache = {}

#     return max_profit_memo(price_list, count, max_profit_cache)


# # 테스트
# print(max_profit([0, 100, 400, 800, 900, 1000], 5))
# print(max_profit([0, 100, 400, 800, 900, 1000], 10))
# print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))