n = int(input())
total = 0
for _ in range(n):
    a, oper, b = input().split()
    a, b = int(a), int(b)
    if oper == "+":
        total += a + b
    elif oper == "-":
        total += a - b
    elif oper == "*":
        total += a * b
    elif oper == "/":
        total += a // b
print(total)
