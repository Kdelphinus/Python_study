"""2738 행렬 덧셈"""

n, m = map(int, input().split())
a_matrix = [list(map(int, input().split())) for _ in range(n)]
b_matrix = [list(map(int, input().split())) for _ in range(n)]
for a, b in zip(a_matrix, b_matrix):
    for i in range(m):
        print(a[i] + b[i], end=" ")
    print()
