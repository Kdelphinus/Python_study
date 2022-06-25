"""14003 가장 긴 증가하는 부분 수열 5 / O(NlogN)까지 가능"""
from bisect import bisect_left


def LIS(numbers):
    q = []
    tmp = []

    for n in numbers:
        if not q or n > q[-1]:  # q가 비었거나 q의 마지막보다 큰 수가 들어왔을 때
            q.append(n)  # 숫자 추가
            tmp.append((len(q) - 1, n))  # 인덱스와 숫자 추가
        else:  # q의 마지막보다 작은 수가 들어왔을 때
            # n이 들어갈 수 있는 위치에 숫자를 바꿔준다, left를 쓰기에 무조건 더 작은 숫자로 바뀐다
            q[bisect_left(q, n)] = n
            tmp.append((bisect_left(q, n), n))  # 인덱스와 숫자 추가

    # 뒤에서부터 값들을 삽입한다
    ans = []
    idx = len(q) - 1
    for i in range(len(tmp) - 1, -1, -1):
        if tmp[i][0] == idx:
            ans.append(tmp[i][1])
            idx -= 1

    return len(ans), reversed(ans)


num = int(input())
numbers = list(map(int, input().split()))
length, arr = LIS(numbers)
print(length)
print(*arr)
