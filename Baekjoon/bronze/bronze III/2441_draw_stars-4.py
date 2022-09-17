num = int(input())
star = "*"
blank = " "
for i in range(num, 0, -1):
    print(f"{blank * (num - i)}{star * i}")
