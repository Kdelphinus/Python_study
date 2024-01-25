# TODO 시간초과: 10**18까지 들어오는 입력을 어떻게 처리하느냐가 관건일 듯
import sys
from collections import deque


INPUT = sys.stdin.readline


def make_one(num: int) -> int:
    queue = deque([(num, 0)])
    while queue:
        n, cnt = queue.popleft()

        if n % 3 == 0:
            if n // 3 == 1:
                return cnt + 1
            queue.append((n // 3, cnt + 1))
        if n % 2 == 0:
            if n // 2 == 1:
                return cnt + 1
            queue.append((n // 2, cnt + 1))
        queue.append((n - 1, cnt + 1))


if __name__ == "__main__":
    NUMBER = int(INPUT())
    print(make_one(NUMBER))
