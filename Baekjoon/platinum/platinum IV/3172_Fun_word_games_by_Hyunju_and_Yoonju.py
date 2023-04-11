# https://www.acmicpc.net/source/18661616 파이썬 풀이, 비트 연산을 활`
import sys

INPUT = sys.stdin.readline

a = [0 for _ in range(100001)]


def get(x):
    t = 0
    while x > 0:
        t += a[x]
        x -= x & -x  # 2진수로 바꾼 x가 가지고 있는 1중 가장 오른쪽에 있는 1만 가짐
    return t


def update(x):
    while x <= 100000:
        a[x] += 1
        x += x & -x  # 2진수로 바꾼 x가 가지고 있는 1중 가장 오른쪽에 있는 1만 가짐


def fun_word_game(n: int, words: list) -> int:
    cnt = 0
    words.sort(key=lambda x: x[0])
    for i in range(n):
        words[i][2] = n - i
    words.sort(key=lambda x: x[1])
    for i in range(n):
        words[i][3] = n - i
    for i in range(n):
        cnt += get(words[i][2])
        update(words[i][2])
    return cnt


if __name__ == "__main__":
    N = int(INPUT())
    W = []
    for _ in range(N):
        word = INPUT().rstrip()
        W.append([word, word[::-1], 0, 0])
    print(fun_word_game(N, W))
