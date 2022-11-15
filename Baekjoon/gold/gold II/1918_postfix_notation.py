# https://pannchat.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-%ED%9B%84%EC%9C%84%ED%91%9C%EA%B8%B0%EC%8B%9D-python

import sys

INPUT = sys.stdin.readline


def postfix_notation(string: str) -> str:
    ans = ""
    stack = []
    for s in string:
        if s.isalpha():
            ans += s
        else:
            if s == "(":
                stack.append(s)
            elif s == "*" or s == "/":
                while stack and (stack[-1] == "*" or stack[-1] == "/"):
                    ans += stack.pop()
                stack.append(s)
            elif s == "+" or s == "-":
                while stack and stack[-1] != "(":
                    ans += stack.pop()
                stack.append(s)
            elif s == ")":
                while stack and stack[-1] != "(":
                    ans += stack.pop()
                stack.pop()
    while stack:
        ans += stack.pop()
    return ans


if __name__ == "__main__":
    print(postfix_notation(INPUT().rstrip()))
