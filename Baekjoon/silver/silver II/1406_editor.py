import sys

INPUT = sys.stdin.readline


def INPUT_alphabet(s: str, a: str, c: int) -> (str, int):
    """
    커서 왼쪽에 문자를 추가하는 함수
    Args:
        s: 현재 문자열
        a: 추가할 문자
        c: 현재 커서 위치

    Returns:
        입력한 후 문자열과 커서 위치
    """
    return s[:c] + a + s[c:], c + 1


def backspace(s: str, c: int) -> (str, int):
    """
    커서 왼쪽의 문자를 지우는 함수
    Args:
        s: 현재 문자열
        c: 현재 커서 위치

    Returns:
        지운 후 문자열과 커서 위치
    """
    return s[: c - 1] + s[c:], c - 1


def editor(s: str) -> str:
    """
    문장 편집기
    Args:
        s: 주어진 문자열

    Returns:
        s: 편집된 문자열

    """
    c = len(s)
    for _ in range(int(INPUT())):
        orders = list(INPUT().split())
        if orders[0] == "L" and c > 0:
            c -= 1
        elif orders[0] == "D" and c < len(s):
            c += 1
        elif orders[0] == "B" and c > 0:
            s, c = backspace(s, c)
        elif orders[0] == "P":
            s, c = INPUT_alphabet(s, orders[1], c)
    return s


if __name__ == "__main__":
    print(editor(INPUT().rstrip()))
