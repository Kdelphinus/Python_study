def reverse_word(s: str) -> str:
    ans = ""
    start, mid, end = len(s), 0, -1
    while True:
        start = s.find("<", mid)
        if start == -1:
            for w in s[end + 1 :].split(" "):
                ans += "".join(reversed(w)) + " "
            return ans[:-1]
        else:
            for w in s[end + 1 : start].split(" "):
                ans += "".join(reversed(w)) + " "
            ans = ans[:-1]
        end = s.find(">", mid)
        ans += s[start : end + 1]
        mid = end + 1


if __name__ == "__main__":
    print(reverse_word(input()))

"""
치환해서 자른 경우

from sys import stdin


def sol(seq: str) -> str:
    seq: list = seq.replace('>', '<').split('<')
    ans: str = ''

    for i in range(len(seq)):
        if i % 2 == 1:
            ans += f'<{seq[i]}>'
        else:
            ans += reverse_words(seq[i])
    return ans


def reverse_words(words: str) -> str:
    return ' '.join(word[::-1] for word in words.split())


print(sol(stdin.readline().rstrip()))
"""
