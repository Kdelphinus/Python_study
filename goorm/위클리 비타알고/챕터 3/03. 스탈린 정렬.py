# 백준 27-3번 문제 / 백준 15-11 방법으로 풀면 시간초과

from bisect import bisect_left


def LIS(numbers):
    q = []

    for n in numbers:
        if not q or n > q[-1]:  # q가 비었거나 q의 마지막보다 큰 수가 들어왔을 때
            q.append(n)  # 숫자 추가
        else:  # q의 마지막보다 작은 수가 들어왔을 때
            # n이 들어갈 수 있는 위치에 숫자를 바꿔준다, left를 쓰기에 무조건 더 작은 숫자로 바뀐다
            q[bisect_left(q, n)] = n

    return len(q)


num = int(input())
numbers = list(map(int, input().split()))
length = LIS(numbers)
print(num - length)  # 삭제하는 개수
