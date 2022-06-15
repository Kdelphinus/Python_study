"""12015 가장 긴 증가하는 부분 수열 2"""
import sys

inpupt = sys.stdin.readline


def binary_search(num):
    """자신보다 큰 값 중 최솟값의 위치를 찾는 함수"""
    start = 0
    end = len(LIS) - 1
    index = 1000000

    while start <= end:
        mid = (start + end) // 2
        if LIS[mid] >= num:
            if index > mid:
                index = mid
            end = mid - 1
        else:
            start = mid + 1

    return index


num = int(input())
number = list(map(int, input().split()))
LIS = [number[0]]

for i in range(1, num):
    if LIS[-1] < number[i]:  # 직전 숫자보다 크다면 LIS에 추가
        LIS.append(number[i])
    else:  # 직전 숫자보다 작거나 같다면 자신보다 큰 수 중 최솟값과 값을 바꾼다
        LIS[binary_search(number[i])] = number[i]

# 이 방식은 O(nlogn)으로 동적 계획법에 비해 빠르지만 LIS의 답을 구할 수는 없다
# 그러나 27-3번 문제는 속도를 빠르게 유지하고 답을 구할 수 있도록 구현
print(len(LIS))
