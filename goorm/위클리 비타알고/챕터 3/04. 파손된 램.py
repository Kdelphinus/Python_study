"""비트를 이용해 푸는 방법"""
"""
2의 제곱수는 가장 앞만 1이고 나머지는 모두 0이다.
(2의 제곱수 - 1)은 2의 제곱수보다 길이가 하나 짧고 모두 1이다.

즉, 예를 들어 1000(=16)이 있으면 0111(=15)가 된다. 
따라서 2의 제곱수와 (2의 제곱수 - 1)의 비트 연산자 &를 하면 0이 나온다.
"""
num = int(input())
ram = list(map(int, input().split()))

broken = []
for idx, r in enumerate(ram):
    if bin(bin(r) & bin(r - 1)) == "0":
        broken.append(idx + 1)

if broken:
    print(len(broken))
    print(*broken)
else:
    print(0)


# ---------------------------------------------------------------------------------

"""2의 제곱승을 모두 구해 확인하는 방법"""
num = int(input())
ram = list(map(int, input().split()))
two_square = [2 ** i for i in range(1, 31)]

broken = []
for idx, r in enumerate(ram):
    if r not in two_square:
        broken.append(idx + 1)

if broken:
    print(len(broken))
    print(*broken)
else:
    print(0)

