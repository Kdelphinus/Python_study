# 투 포인터 사용
length, target = map(int, input().split())
fish = list(map(int, input().split()))

cnt, start, end = 0, 0, 1
while start < end:
    # 구간합이 목적치보다 크면 앞쪽 포인터를 뒤로 미룬다.
    if sum(fish[start:end]) > target:
        start += 1
        if start == end:
            end += 1
    # 구간합이 목적치보다 작으면 뒤쪽 포인터를 뒤로 미룬다.
    elif sum(fish[start:end]) < target:
        end += 1
    # 구간합이 목적치와 동일하면 cnt를 추가하고 두 포인터 모두 뒤로 미룬다.
    # 최소 한 마리씩 있기에 뒤에 0마리가 있는 경우의 수는 확인 안 해도 된다.
    else:
        cnt += 1
        start += 1
        end += 1

    # 마지막까지 확인하면 종료
    if end == length + 1:
        break

print(cnt)

# ========================================================================================

# 부분합을 활용 / 시간초과
"""
length, target = map(int, input().split())
fish = list(map(int, input().split()))

partial_sum = [0]
for f in fish:
    partial_sum.append(f + partial_sum[-1])

cnt = 0
for i in range(1, length + 1):
    if fish[i - 1] == target:
        cnt += 1

    for j in range(1, i):
        if partial_sum[i] - partial_sum[j - 1] == target:
            cnt += 1

print(cnt)
"""
