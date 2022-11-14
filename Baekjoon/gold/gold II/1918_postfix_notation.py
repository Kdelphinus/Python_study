# 반례: G*(A-B*(C/D+E)/F)
# 현재 (의 우선순위가 연산자의 우선순위보다 밀림

import sys

INPUT = sys.stdin.readline


def postfix_notation(string: str) -> str:
    ans = ""
    i = 0
    bracket, operator = [], []
    while i < len(string):
        if string[i] == "(":
            bracket.append(1)
        elif string[i] == ")":
            bracket.pop()
            for _ in range(2):
                if operator:
                    ans += operator.pop()
        elif string[i] == "+" or string[i] == "-":
            operator.append(string[i])
        elif string[i] == "*" or string[i] == "/":
            if string[i + 1] == "(":
                operator.append(string[i])
            else:
                ans += string[i + 1]
                ans += string[i]
                i += 1
                while operator:
                    ans += operator.pop()
        else:
            ans += string[i]
        i += 1
    while operator:
        ans += operator.pop()
    return ans


if __name__ == "__main__":
    print(postfix_notation(INPUT().rstrip()))
