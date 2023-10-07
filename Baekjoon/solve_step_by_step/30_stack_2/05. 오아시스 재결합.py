"""3015 오아시스 재결합"""
# 풀이: https://mingchin.tistory.com/m/425

import sys

INPUT = sys.stdin.readline

if __name__ == "__main__":
    ans, n, stack = 0, int(INPUT()), []
    for _ in range(n):
        num = int(INPUT())

        # 스택 마지막 사람보다 키 큰 사람이 들어왔을 때
        while stack and stack[-1][0] < num:
            ans += stack.pop()[1]

        # 스택이 비었을 때
        if not stack:
            stack.append((num, 1))
        # 같은 키 일때
        # 같은 키까지는 볼 수 있기에 빼는 것에 걸리게 하는 것 대신 cnt를 활용하여 중첩처리
        elif stack[-1][0] == num:
            cnt = stack.pop()[1]
            ans += cnt
            if stack:
                ans += 1
            stack.append((num, cnt + 1))
        # 그 외는 추가
        else:
            stack.append((num, 1))
            ans += 1
    print(ans)
