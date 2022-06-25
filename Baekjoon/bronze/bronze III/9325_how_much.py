t = int(input())
for _ in range(t):
    price = int(input())
    n = int(input())
    for i in range(n):
        num, option = map(int, input().split())
        price += num * option
    print(price)
