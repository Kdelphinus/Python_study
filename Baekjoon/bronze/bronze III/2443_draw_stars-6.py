n = int(input())
star, blank = "*", " "
for i in range(n, 0, -1):
    print(blank * (n - i), end="")
    print(star * (2 * i - 1))
