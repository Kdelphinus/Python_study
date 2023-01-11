def is_Luhn(num: str) -> str:
    total = 0
    for i, n in enumerate(num):
        tmp = int(n)
        if i % 2:
            tmp *= 2
            if tmp > 9:
                tmp = tmp // 10 + tmp % 10
        total += tmp
    return "F" if total % 10 else "T"


t = int(input())
for _ in range(t):
    credit_number = input()
    print(is_Luhn(credit_number[::-1]))
