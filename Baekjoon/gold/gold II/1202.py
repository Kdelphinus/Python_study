# https://bio-info.tistory.com/195

import sys
import heapq

INPUT = sys.stdin.readline


def steal_jewels(jewels: list[tuple[int, int]], bags: list[int]) -> int:
    tmp, max_price = [], 0
    jewels.sort()
    bags.sort()
    for bag in bags:
        while jewels and jewels[0][0] <= bag:
            heapq.heappush(tmp, -jewels[0][1])  # 가격을 최대힙에 저장
            heapq.heappop(jewels)
        if tmp:  # 넣을 수 있는 보석 중에서 가장 큰 것 넣기
            max_price -= heapq.heappop(tmp)
    return max_price


if __name__ == "__main__":
    N, K = map(int, INPUT().split())
    JEWELS = [tuple(map(int, INPUT().split())) for _ in range(N)]
    BAGS = [int(INPUT()) for _ in range(K)]
    print(steal_jewels(JEWELS, BAGS))
