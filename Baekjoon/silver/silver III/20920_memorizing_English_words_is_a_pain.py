import sys
from collections import defaultdict

INPUT = sys.stdin.readline


def e_word(n: int, m: int):
    words = defaultdict(int)
    for _ in range(n):
        word = INPUT().rstrip()
        if len(word) >= m:
            words[word] += 1
    words = list(words.items())
    words.sort(key=lambda x: (-x[1], -len(x[0]), x[1]))
    for w, d in words:
        print(w)


if __name__ == "__main__":
    N, M = map(int, INPUT().split())
    e_word(N, M)
