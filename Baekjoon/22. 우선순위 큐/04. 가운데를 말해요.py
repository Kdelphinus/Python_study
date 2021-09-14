"""1655 가운데를 말해요"""
import sys
import heapq


input = sys.stdin.readline
num = int(input())
small_heap = []  # 중간값보다 작거나 같은 값을 넣을 최대힙
big_heap = []  # 중간값보다 큰 값을 넣을 최소힙

for i in range(num):
    order = int(input())

    if len(small_heap) > len(big_heap):  # 작은 값을 가진 힙이 큰 값을 가진 힙보다 개수가 많다면
        if order < small_heap[0][1]:  # 넣을 값이 작은 값을 가진 힙의 최댓값보다 작다면
            heapq.heappush(small_heap, (-order, order))  # 작은 값을 가진 힙에 넣고
            temp = heapq.heappop(small_heap)[1]  # 최댓값을 빼서
            heapq.heappush(big_heap, temp)  # 큰 값을 가진 힙에 넣는다
        else:  # 넣을 값이 작은 값을 가진 힙의 최댓값보다 크다면
            heapq.heappush(big_heap, order)  # 큰 값을 가진 힙에 넣는다
    else:  # 두 힙의 길이가 같다면(큰 값을 가진 힙이 작은 값을 가진 힙보다 길 수는 없다)
        if not small_heap:  # 처음 시작일 때
            heapq.heappush(small_heap, (-order, order))  # 작은 값을 가진 힙에 넣는다
        else:  # 처음 값이 아니라면
            if order > big_heap[0]:  # 큰 값을 가진 힙의 최솟값보다 크면
                heapq.heappush(big_heap, order)  # 큰 값을 가진 힙에 넣고
                temp = heapq.heappop(big_heap)  # 큰 값을 가진 힙의 최솟값을 뺀 뒤
                heapq.heappush(small_heap, (-temp, temp))  # 작은 값을 가진 힙에 넣는다
            else:  # 큰 값을 가진 힙의 최솟값보다 작다면
                heapq.heappush(small_heap, (-order, order))  # 작은 값을 가진 힙에 넣는다

    print(small_heap[0][1])  # 중간값은 항상 작은 값을 가지는 힙의 최댓값이다(개수가 짝수일 때 작은 것을 중간값으로 하기에)
