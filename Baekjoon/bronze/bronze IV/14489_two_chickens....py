A, B = map(int, input().split())
C = int(input())
print(A + B - C * 2) if A + B >= C * 2 else print(A + B)
