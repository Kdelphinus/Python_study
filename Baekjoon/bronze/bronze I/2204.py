n = int(input())
while n:
    words = []
    for _ in range(n):
        tmp = input()
        words.append((tmp, tmp.lower()))
    words.sort(key=lambda x: x[1])
    print(words[0][0])
    n = int(input())