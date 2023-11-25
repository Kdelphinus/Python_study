def postfix_notation(numbers: list[int], eq: str) -> float:
    stack = []
    for e in eq:
        if e in ("+", "-", "*", "/"):
            b = stack.pop()
            a = stack.pop()
            if e == "+":
                stack.append(a + b)
            elif e == "-":
                stack.append(a - b)
            elif e == "*":
                stack.append(a * b)
            elif e == "/":
                stack.append(a / b)
        else:
            stack.append(numbers[ord(e) - ord("A")])
    return stack[0]


if __name__ == "__main__":
    N = int(input())
    EQUATION = input()
    NUMBERS = [int(input()) for _ in range(N)]
    print(f"{postfix_notation(NUMBERS, EQUATION):.2f}")
