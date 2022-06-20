import sys
import heapq as hq


def main():
    num = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    for _ in range(num):
        number = int(sys.stdin.readline())

        if not min_heap:
            hq.heappush(min_heap, (-number, number))
        elif len(min_heap) > len(max_heap):
            if min_heap[0][1] < number:
                hq.heappush(max_heap, number)
            else:
                _, tmp = hq.heappop(min_heap)
                hq.heappush(min_heap, (-number, number))
                hq.heappush(max_heap, tmp)
        elif len(min_heap) == len(max_heap):
            if max_heap[0] < number:
                tmp = hq.heappop(max_heap)
                hq.heappush(min_heap, (-tmp, tmp))
                hq.heappush(max_heap, number)
            else:
                hq.heappush(min_heap, (-number, number))
        print(min_heap[0][1])


if __name__ == "__main__":
    main()
