n = int(input())
star, blank = "*", " "
for i in range(1, n + 1):
    print(f"{star * i}{blank * (2 * (n - i))}{star * i}")
for i in range(n - 1, 0, -1):
    print(f"{star * i}{blank * (2 * (n - i))}{star * i}")
