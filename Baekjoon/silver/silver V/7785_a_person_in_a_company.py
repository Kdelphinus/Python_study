import sys

INPUT = sys.stdin.readline

num = int(input())
names = set()
for _ in range(num):
    name, state = INPUT().rstrip().split()
    if state == "enter":
        names.add(name)
    else:
        names.remove(name)

for name in sorted(names, reverse=True):
    print(name)
