price, num, money = map(int, input().split())
add_money = price * num - money
print(add_money if add_money >= 0 else 0)
