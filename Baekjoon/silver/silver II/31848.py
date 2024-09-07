# jh502125님의 풀이
import sys

INPUT = sys.stdin.readline


def acorn_classification():
    size = [0] * (N + 1)
    now = 0  # 현재 구멍 위치
    for i in range(1, N + 1):  # 전체 도토리 크기 확인하기
        while (
            i - now > HOLES[now]
        ):  # 구멍을 지나온 도토리 크기가 구멍보다 크다면 다음 구멍으로 이동
            now += 1
        size[i] = now + 1  # 들어갈 수 있는 구멍을 찾았다면 저장

    for acorn in ACORNS:
        print(size[acorn], end=" ")


if __name__ == "__main__":
    N = int(INPUT())
    HOLES = list(map(int, INPUT().split()))
    Q = int(INPUT())
    ACORNS = list(map(int, INPUT().split()))
    acorn_classification()
