n = int(input())
starb, blank = "* ", " "
for i in range(1, n + 1):
    print(f"{blank * (n - i)}{starb * i}")
