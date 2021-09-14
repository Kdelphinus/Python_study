def solution(arr):
    if len(arr) <= 1:  # 수가 1개 이하로 들어있으면 남는 것이 없음
        return [-1]

    n = arr.index(min(arr))  # 가장 작은 수의 인덱스를 구하고
    del arr[n]  # 그 인덱스를 제거
    return arr
