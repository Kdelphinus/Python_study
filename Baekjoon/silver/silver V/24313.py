"""
c >= a1이 들어가야 하는 이유
https://kevinitcoding.tistory.com/entry/%EB%B0%B1%EC%A4%80Python-24313%EB%B2%88-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%88%98%EC%97%85-%EC%A0%90%EA%B7%BC%EC%A0%81-%ED%91%9C%EA%B8%B0-1-%EB%AC%B8%EC%A0%9C
"""


def big_o(a1: int, a0: int, c: int, n0: int) -> int:
    return 1 if a1 * n0 + a0 <= c * n0 and c >= a1 else 0


if __name__ == "__main__":
    A1, A0 = map(int, input().split())
    C = int(input())
    N0 = int(input())
    print(big_o(A1, A0, C, N0))
