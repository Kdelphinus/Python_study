n = int(input())
ball = 1
for _ in range(n):
    x, y = map(int, input().split())
    if ball == x:
        ball = y
    elif ball == y:
        ball = x
print(ball)
