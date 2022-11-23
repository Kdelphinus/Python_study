# 해설링크: https://seongonion.tistory.com/53

import sys

INPUT = sys.stdin.readline


def editor(s: str) -> str:
    """
    두 개의 스택으로 커서의 위치를 표현하여 에디터를 작동하는 함수
    Args:
        s: 주어진 문자열

    Returns:
        모든 작업이 끝난 문자열

    """
    stack1, stack2 = list(s), []  # 커서를 기준으로 앞 뒤를 두 개의 스택으로 나눔
    for _ in range(int(INPUT())):
        command = list(INPUT().split())
        if command[0] == "L" and stack1:
            stack2.append(stack1.pop())
        elif command[0] == "D" and stack2:
            stack1.append(stack2.pop())
        elif command[0] == "B" and stack1:
            stack1.pop()
        elif command[0] == "P":
            stack1.append(command[1])
    return "".join(stack1 + stack2[::-1])


if __name__ == "__main__":
    print(editor(INPUT().rstrip()))
