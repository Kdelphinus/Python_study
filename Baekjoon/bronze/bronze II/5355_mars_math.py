test = int(input())
for t in range(test):
    operation = list(input().split())
    num = float(operation[0])
    for idx, oper in enumerate(operation[1:]):
        if oper == "@":
            num *= 3
        elif oper == "%":
            num += 5
        elif oper == "#":
            num -= 7
    print(f"{num:.2f}")
