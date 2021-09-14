from collections import Counter

num = ["a", "b", "b", "b", "b", "c", "c", "c", "h", "h", "e", "o"]

# 원소가 몇개있는지 세고 딕셔너리 형식으로 저장
mode = Counter(num)
print(mode)

# key 값 리스트로 만들기
print(list(mode.keys()))

# value 값 리스트로 만들기
print(list(mode.values()))

# key, value 형태의 이차원 배열로 저장
# 빈도수가 많은 순서대로 저장됨
print(mode.most_common())

# -------------------------------------------------------------------------------------

"""deque"""
from collections import deque

cache = deque(maxlen=5)
for i in range(1, 11):
    cache.append(i)
# 최대 길이에 도달하면 가장 오래된 것이 사라지고 최근 것이 들어간다
print(cache)  # deque([6, 7, 8, 9, 10], maxlen=5)

# -------------------------------------------------------------------------------------

"""defaultdict"""
from collections import defaultdict

# defaultdict은 지정하지 않은 키가 들어올 때 default 값으로 지정해주는 사전이다
# int외에도 list, set 등을 줄 수도 있다, 이들의 default는 모두 비어있는 list, set이다
int_dict = defaultdict(int)
int_dict["A"]  # default값인 0이 배정
int_dict["B"] = 2
print(int_dict)  # defaultdict(<class 'int'>, {'A': 0, 'B' : 2})


# defaultdict(int) 활용 예제
letters = "ko myoung jun"
letters_dict = defaultdict(int)
for l in letters:
    letters_dict[l] += 1

# 알파벳 개수가 value로 저장된다
# defaultdict(<class 'int'>, {'k': 1, 'o': 2, ' ': 2, 'm': 1, 'y': 1, 'u': 2, 'n': 2, 'g': 1, 'j': 1})
print(letters_dict)


namelist = [
    ("kim", "sungsu"),
    ("kang", "hodong"),
    ("park", "jisung"),
    ("kim", "yuna"),
    ("park", "chanho"),
    ("kang", "hodong"),
]
ndict = defaultdict(list)
for k, v in namelist:
    ndict[k].append(v)
print(ndict)
# defaultdict(<class 'list'>, {'kim': ['sungsu', 'yuna'], 'kang': ['hodong', 'hodong'], 'park': ['jisung', 'chanho']})
# 성에 따라서 이름이 나누어지지만 중복은 제거되지 않음

nset = defaultdict(set)
for k, v in namelist:
    nset[k].add(v)
print(nset)
# defaultdict(<class 'set'>, {'kim': {'yuna', 'sungsu'}, 'kang': {'hodong'}, 'park': {'chanho', 'jisung'}})
# set을 이용하면 중복값은 사라진다

# -------------------------------------------------------------------------------------
