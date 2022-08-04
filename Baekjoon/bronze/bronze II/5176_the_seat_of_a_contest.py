t = int(input())
for _ in range(t):
    p, m = map(int, input().split())
    seat = set()
    for i in range(p):
        seat.add(int(input()))
    print(p - len(seat))
