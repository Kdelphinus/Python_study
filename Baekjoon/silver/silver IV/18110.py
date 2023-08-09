# round함수에 대해
# https://m.blog.naver.com/PostView.nhn?blogId=herbdoc95&logNo=221574077380&proxyReferer=http:%2F%2Fblog.naver.com%2FPostView.nhn%3FblogId%3Dherbdoc95%26logNo%3D221574077380
import sys

INPUT = sys.stdin.readline


def round2(n: float) -> int:
    return int(n) + (1 if n - int(n) >= 0.5 else 0)


def measure_difficulty(n: int, level: list) -> int:
    if n == 0:
        return 0
    level.sort()
    boundary = round2(n * 0.15)
    return round2(sum(level[boundary : n - boundary]) / (n - boundary * 2))


if __name__ == "__main__":
    N = int(INPUT())
    LEVEL = []
    for _ in range(N):
        LEVEL.append(int(INPUT()))
    print(measure_difficulty(N, LEVEL))
