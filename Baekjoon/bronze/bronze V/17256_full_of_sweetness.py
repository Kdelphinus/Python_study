ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())
print(f"{cx - az} {cy // ay} {cz - ax}")
