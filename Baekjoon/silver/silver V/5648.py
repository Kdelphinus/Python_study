import sys

INPUT = sys.stdin.readline

lst = list(INPUT().rstrip().split())
cnt = int(lst[0])
lst = list(int(i[::-1]) for i in lst[1:])
while len(lst) != cnt:
    lst += list(map(int, INPUT().rstrip()[::-1].split()))
for i in sorted(lst):
    print(i)
