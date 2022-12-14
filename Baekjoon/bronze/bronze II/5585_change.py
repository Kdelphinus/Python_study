cnt, money = 0, 1000 - int(input())
for i in (500, 100, 50, 10, 5, 1):
    cnt += money // i
    money %= i
    if money == 0:
        break
print(cnt)
