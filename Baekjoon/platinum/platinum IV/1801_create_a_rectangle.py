# zz79ya의 풀이

N = int(input())
S = [0] * (1 << N)
D = [False] * (1 << N)
X = list(map(int, input().split()))
for i in range(N):
    S[1 << i] = X[i]

for i in range(1, 1 << N):
    x = i & -i
    if i == x:
        continue
    S[i] = S[i - x] + S[x]

for i in range(1, 1 << N):
    if S[i] & 1 == 0:
        j = (i - 1) & i
        while not D[i] and j:
            D[i] = S[j] == S[i - j]
            j = (j - 1) & i

ans = -1
for i in range(1, 1 << N):
    j = (i - 1) & i
    while j:
        if D[j] and D[i - j]:
            a = S[j] * S[i - j] // 4
            ans = max(ans, a)
        j = (j - 1) & i
print(ans)
