"""실제로 내림차순하는 것이 아닌 내림차순 했다고 가정하는 것이 시간을 줄이는 키포인트"""
num = int(input())
cnt = 0
stack = []
block = 0
pass_cnt = 0
for _ in range(2 * num):
    order, *n = input().split()
    if order == "add":
        n = int(n[0])
        stack.append(n)
    else:
        if not stack and pass_cnt > 0:  # 건너뛸 횟수가 남았을 때
            pass_cnt -= 1  # 하나 건너뜀
            block += 1  # 블록 하나를 뺌
            continue

        if stack[-1] != block + 1:  # 스택을 내림차순 해야할 때
            cnt += 1
            pass_cnt += len(stack) - 1  # 내림차순했다고 치기 위해 remove를 pass_cnt번 건너뜀
            stack.clear()  # 내림차순 되어있는 스택은 비워버림
        else:  # 지금 빼야 하는 블록일 때
            stack.pop()  # 맨 위 블록만 뺌
        block += 1  # 블록 하나를 정리함
print(cnt)

# --------------------------------------------------------

# 마지막 테스트 케이스 시간 초과
"""
num = int(input())
cnt = 0
stack = []
block = [0]
for _ in range(2 * num):
    order, *n = input().split()
    if order == "add":
        n = int(n[0])
        stack.append(n)
    else:
        if stack[-1] != block[-1] + 1:
            stack.sort(reverse=True) # 최선의 방법은 내림차순으로 순서를 바꾸는 것
            cnt += 1
        stack.pop()
        block.append(block[-1] + 1)
print(cnt)
"""
