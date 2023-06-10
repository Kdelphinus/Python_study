"""13241 최소공배수"""


def gcd(a: int, b: int) -> int:
    """최대 공약수"""
    return gcd(b, a % b) if b else a


def lcm(a: int, b: int) -> int:
    """최소 공배수"""
    return a * b // gcd(a, b)


if __name__ == "__main__":
    A, B = map(int, input().split())
    print(lcm(A, B))
