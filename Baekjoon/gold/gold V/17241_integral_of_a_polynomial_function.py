def eq_split(eq: str) -> list:
    """
    방정식을 나누는 함수
    Args:
        eq: 문자열로 주어진 방정식

    Returns:
        result: 나뉘어진 방정식의 계수와 차수
    """
    s, e, result = 0, 0, list()
    while e < len(eq):
        while e < len(eq) and eq[e] != "x":
            e += 1
        result.append([int(eq[s:e])])
        s = 0
        while e < len(eq) and eq[e] == "x":
            s += 1
            e += 1
        result[-1].append(s)
        s = e
    return result


def my_integral(eq: str) -> str:
    """
    적분한 방정식을 반환하는 함수
    Args:
        eq: 주어진 방정식

    Returns:
        ans: 적분된 방정식
    """
    if eq == "0":
        return "W"
    ans, eq = "", eq_split(eq)
    for c, r in eq:
        c = c // (r + 1)
        if ans and ans[-1] == "x" and c >= 0:
            ans += "+"
        if abs(c) != 1:
            ans += str(c)
        elif c == -1:
            ans += "-"
        ans += "x" * (r + 1)
    ans += "+W"
    return ans


if __name__ == "__main__":
    print(my_integral(input()))
