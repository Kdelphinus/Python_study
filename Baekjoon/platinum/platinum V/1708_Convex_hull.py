# 링크: https://johoonday.tistory.com/205
# 두 점 사이 각도: https://blog.naver.com/PostView.naver?blogId=rheesungjun&logNo=222366320312
# 반례들: https://www.acmicpc.net/board/view/77243
import sys
import math

INPUT = sys.stdin.readline


def ccw(d1: tuple, d2: tuple, d3: tuple) -> int:
    """
    Counter Clock Wise 알고리즘: 평면에 존재하는 세 점에 대해서 위치 관계를 알 수 있는 함수
    Args:
        d1: 첫번째 점
        d2: 두번째 점
        d3: 세번째 점

    Returns:
        양수: 선분 d1d2에 대해서 점 d3는 반시계 방향에 위치
        음수: 선분 d1d2에 대해서 점 d3는 시계 방향에 위치
        0: 선분 d1d2와 점 d3는 직선

    """
    return (d2[0] - d1[0]) * (d3[1] - d1[1]) - (d3[0] - d1[0]) * (d2[1] - d1[1])


def convex_hull(n: int, d: list) -> int:
    # 일반적으로 y가 가장 작은 좌표를 고른다.
    d = sorted(d, key=lambda x: (x[1], x[0]))
    s = d[0]

    # s를 기준으로 반시계 정렬
    d = sorted(d[1:], key=lambda x: (math.atan2(x[1] - s[1], x[0] - s[0]), abs(x[0])))

    # 마지막 점도 확인하기 위해 마지막에 s 추가
    d.append(s)
    stack = [s, d[0]]

    for idx, third in enumerate(d[1:]):
        while len(stack) > 1:
            second = stack.pop()
            # third가 반시계 방향에 있으면 second를 추가
            if ccw(stack[-1], second, third) > 0:
                stack.append(second)
                break
        if idx < n - 2:  # third를 스택에 추가, 추가한 s는 다시 추가하지 않는 조건
            stack.append(third)

    return len(stack)  # 2022.12.13 기준 직선으로 만들어지면 1, 2 아무거나 해도 되는 듯


if __name__ == "__main__":
    N = int(INPUT())
    dots = [tuple(map(int, input().split())) for _ in range(N)]
    print(convex_hull(N, dots))
