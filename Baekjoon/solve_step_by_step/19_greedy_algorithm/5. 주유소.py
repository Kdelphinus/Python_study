"""13305 주유소"""

num = int(input())  # 도시의 개수
length = list(map(int, input().split()))  # 도시 사이의 거리
price = list(map(int, input().split()))  # 리터당 가격

start = 0  # 주유할 곳
min_price = price[0]  # 지금까지 지나간 곳 중 가장 싼 가격
total_price = 0  # 총 가격

for i in range(num - 1):  # 도착 직전 도시까지만 본다
    if min_price >= price[i + 1]:  # 다음 도시가 지금까지의 최저 가격보다 싸다면
        total_price += sum(length[start : i + 1]) * min_price  # 지금까지 거리의 기름을 구입하고
        min_price = price[i + 1]  # 다음 도시 가격으로 최저가를 바꾼 후
        start = i + 1  # 기름을 새로 사는 도시도 바꾼다

    if i == num - 2:  # 도착 직전 도시까지 오면 지금까지의 거리만큼 주유한다
        total_price += sum(length[start : i + 1]) * min_price


print(total_price)
