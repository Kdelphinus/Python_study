def min_coin_count(value, coin_list):
    coin_list.sort()
    i = len(coin_list) - 1
    cnt = 0
    while value != 0:
        if value >= coin_list[i]:
            value -= coin_list[i]
            cnt += 1
        else:
            i -= 1
    return cnt


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))


# 해답
def min_coin_count(value, coin_list):
    # 누적 동전 개수
    count = 0

    # coin_list의 값들을 큰 순서대로 본다
    for coin in sorted(coin_list, reverse=True):
        # 현재 동전으로 몇 개 거슬러 줄 수 있는지 확인한다
        count += value // coin

        # 잔액을 계산한다
        value %= coin

    return count