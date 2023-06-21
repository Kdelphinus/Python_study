test = int(input())

for i in range(test):
    day = int(input())
    price = list(map(int, input().split()))
    count = 0
    sell_price = price[-1]  # 마지막 날짜를 판매 금액으로 설정
    total = 0

    for j in range(len(price) - 2, -1, -1):  # 뒤에서부터 확인
        if sell_price > price[j]:  # 판매금액이 전날 금액보다 클 경우
            total += sell_price - price[j]  # 차액을 더함
        else:  # 판매금액이 전날 금액보다 같거나 작다면 판매금액 변경
            sell_price = price[j]

    print("#{} {}".format(i + 1, total))

# test
# 3
# 3
# 10 7 6
# 3
# 3 5 9
# 5
# 1 1 3 1 2
