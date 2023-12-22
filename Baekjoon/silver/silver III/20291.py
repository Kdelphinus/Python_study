import sys
from collections import defaultdict

INPUT = sys.stdin.readline


n = int(INPUT())
file_dictionary = defaultdict(int)
for _ in range(n):
    file = tuple(INPUT().rstrip().split("."))
    file_dictionary[file[-1]] += 1
for extension, num in sorted(file_dictionary.items()):
    print(extension, num)
