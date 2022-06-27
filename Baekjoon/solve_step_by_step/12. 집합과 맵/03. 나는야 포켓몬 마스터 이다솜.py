"""1620 나는야 포켓몬 마스터 이다솜 / 실버 IV"""

import sys
from collections import defaultdict

INPUT = sys.stdin.readline

n, m = map(int, INPUT().split())
pokemon_number = defaultdict()  # key: number, value: name
pokemon_name = defaultdict()  # key: name, value: number
for i in range(1, n + 1):
    name = INPUT().rstrip()  # \n을 제거하기 위함
    pokemon_name[name] = i
    pokemon_number[i] = name

for _ in range(m):
    tmp = INPUT().rstrip()  # \n을 제거하기 위함
    if tmp.isdigit():
        print(pokemon_number[int(tmp)])
    else:
        print(pokemon_name[tmp])
