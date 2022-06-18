num = int(input())
quadrant = {
    "Q1": 0,
    "Q2": 0,
    "Q3": 0,
    "Q4": 0,
    "AXIS": 0,
}
for _ in range(num):
    x, y = map(int, input().split())
    if x * y == 0:
        quadrant["AXIS"] += 1
    elif x > 0 and y > 0:
        quadrant["Q1"] += 1
    elif x < 0 and y > 0:
        quadrant["Q2"] += 1
    elif x < 0 and y < 0:
        quadrant["Q3"] += 1
    elif x > 0 and y < 0:
        quadrant["Q4"] += 1

for name, cnt in quadrant.items():
    print(f"{name}: {cnt}")
