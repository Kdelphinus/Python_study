import heapq

heap = []  # 최소 힙 생성

"""힙에 원소 추가"""
heapq.heappush(heap, 7)
heapq.heappush(heap, 2)
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)

# 힙의 속성을 유지한 상태에서 추가됨(O(logN))
print(heap)  # [1, 2, 5, 7]


"""힙에서 원소 삭제"""
# 가장 작은 원소 삭제
print(heapq.heappop(heap))  # 1
print(heap)  # [2, 5, 7]


"""힙에서 최솟값 불러오기"""
print(heap[0])  # 2
# 그러나 두 번째로 작은 값은 heap[1]이 아니다
# 힙 속성에 맞춰서 정렬되어 있기에 최솟값만 인덱스로 바로 불러올 수 있다


"""기존 리스트를 힙으로 변환"""
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)  # 힙으로 변환(O(N))
print(heap)  # [1, 3, 5, 4, 8, 7]


"""최대 힙"""
# 힙은 최솟값만 구할 수 있기에 응용이 필요
nums = [4, 1, 7, 3, 8, 5]
heap = []

# 튜플대신 값만 음수로 바꾸어 추가하고 출력할 때 다시 양수로 바꿔도 된다
for num in nums:
    heapq.heappush(heap, (-num, num))  # (우선 순위, 원래 값), 우선 순위 순으로 정렬되고 같을 때 원래값 기준으로 정렬

print(heap)  # [(-8, 8), (-7, 7), (-5, 5), (-1, 1), (-3, 3), (-4, 4)]
print(heapq.heappop(heap)[1])  # 8


"""k번째 최솟값/최댓값"""
# 최댓값이나 최솟값을 k번 호출하면 된다


def kth_smallest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    kth_min = None
    for _ in range(k):
        kth_min = heapq.heappop(heap)
    return kth_min


print(kth_smallest([4, 1, 7, 3, 8, 5], 3))


"""힙 정렬"""


def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums


print(heap_sort([4, 1, 7, 3, 8, 5]))  # [1, 3, 4, 5, 7, 8]
