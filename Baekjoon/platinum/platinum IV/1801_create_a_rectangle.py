# zz79ya의 풀이
# 파이썬에서 음수 비트연산: https://kbj96.tistory.com/28

# 비트의 값이 1이면 그 인덱스의 막대를 사용하고 0이면 그 인덱스의 막대를 사용하지 않음을 표시

N = int(input())  # 막대의 개수
S = [0] * (1 << N)
D = [False] * (1 << N)
X = list(map(int, input().split()))

# 막대를 하나만 사용했을 때, 길이를 S에 저장
for i in range(N):
    S[1 << i] = X[i]

# S[1110] = S[1000] + S[0100] + S[0010]을 해주는 과정
for i in range(1, 1 << N):
    x = i & -i  # i가 가지고 있는 1중 가장 오른쪽에 있는 1만 가짐
    if i == x:  # 2의 제곱수는 이미 위에서 저장했기에 지나감
        continue
    S[i] = S[i - x] + S[x]

# 우선적으로 두 변 먼저 확인
for i in range(1, 1 << N):
    if S[i] & 1 == 0:  # 짝수일 때
        j = (i - 1) & i  # i가 가지고 있는 1중 가장 오른쪽에 있는 1만 0으로 바꿈
        while not D[i] and j:  # 주어진 막대로 만들 수 있는 모든 조합을 확인
            D[i] = S[j] == S[i - j]
            j = (j - 1) & i  # 주어진 조합을 두 개의 서로소인 부분집합으로 나눌 수 있는 모든 경우의 수를 확인

# 가로, 세로를 만들 수 있으면 넓이를 구하여 최댓값 구하기
ans = -1
for i in range(1, 1 << N):
    j = (i - 1) & i
    while j:
        if D[j] and D[i - j]:
            a = S[j] * S[i - j] // 4
            ans = max(ans, a)
        j = (j - 1) & i
print(ans)
