"""1712 손익분기점"""
A, B, C = map(int, input().split())  # A: 고정비용 B: 가변비용 C: 판매가격
if B >= C:
    print(-1)
else:
    print(int(A / (C - B)) + 1)
