"""1735 분수 합"""


def gcd(a: int, b: int) -> int:
    """최대 공약수"""
    return gcd(b, a % b) if b else a


def lcm(a: int, b: int) -> int:
    """최소 공배수"""
    return a * b // gcd(a, b)


def fraction_plus(a1: int, b1: int, a2: int, b2: int) -> tuple:
    denominator = lcm(b1, b2)  # 분모
    numerator = a1 * (denominator // b1) + a2 * (denominator // b2)  # 분자
    gcd_f = gcd(denominator, numerator)
    if gcd_f != 1:
        denominator, numerator = denominator // gcd_f, numerator // gcd_f
    return numerator, denominator


if __name__ == "__main__":
    A1, B1 = map(int, input().split())
    A2, B2 = map(int, input().split())
    print(*fraction_plus(A1, B1, A2, B2))
