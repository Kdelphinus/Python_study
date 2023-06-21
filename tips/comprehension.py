""" 1. list comprehension """
# 20까지의 짝수를 출력하기 위해 다음과 같은 LC를 사용할 수 있다
evens = [x * 2 for x in range(11)]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 리스트의 모든 원소값을 정규화 시킨 후 상수값을 더하는 LC
vals = [32, 12, 96, 42, 32, 93, 31, 23, 65, 43, 76]
amount = sum(vals)
norm_and_move = [(x / amount) + 1 for x in vals]
# [1.0587155963302752, 1.0220183486238532, 1.1761467889908257, 1.0770642201834861, 1.0587155963302752, 1.1706422018348623, 1.0568807339449542, 1.0422018348623854, 1.1192660550458715, 1.0788990825688074, 1.1394495412844037]

# 100 이하의 제곱수가 아닌 수를 찾는 LC
from math import sqrt

non_squars = [x for x in range(101) if sqrt(x) ** 2 != x]
# [2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 18, 19, 20, 23, 24, 26, 28, 29, 31, 32, 37, 38, 40, 43, 45, 48, 50, 51, 52, 58, 59, 60, 61, 63, 65, 66, 72, 73, 75, 76, 77, 78, 80, 82, 87, 89, 92, 94, 95, 96, 97]

# 두 리스트의 원소들의 모든 조합을 찾는 LC
epithets = ["sweet", "annoying", "cool", "grey-eyed"]
names = ["john", "alice", "james"]
epithet_names = [(e, n) for e in epithets for n in names]
# [('sweet', 'john'), ('sweet', 'alice'), ('sweet', 'james'), ('annoying', 'john'), ('annoying', 'alice'), ('annoying', 'james'), ('cool', 'john'), ('cool', 'alice'), ('cool', 'james'), ('grey-eyed', 'john'), ('grey-eyed', 'alice'), ('grey-eyed', 'james')]

# a^2 + b^2 = c^2 (a < b < c)를 만족하는 피타고라스 방정식의 해를 찾는 LC
solutions = [
    (x, y, z)
    for x in range(1, 30)
    for y in range(x, 30)
    for z in range(y, 30)
    if x**2 + y**2 == z**2
]
# [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (10, 24, 26), (12, 16, 20), (15, 20, 25), (20, 21, 29)]

# 단어에서 모음을 제거하는 LC
word = "mathematics"
without_vowels = "".join([c for c in word if c not in ["a", "e", "i", "o", "u"]])
# 'mthmtcs'

# 행렬을 일차원화 시키는 LC
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
flatten = [e for r in matrix for e in r]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# 9 x 9의 숫자를 받는 LC
sudoku = [list(map(int, input().split())) for _ in range(9)]

# -----------------------------------------------------------------------------------------

""" 2. set comprehension """
# 다음의 LC는 중복된 값들을 포함한다
no_primes = [j for i in range(2, 9) for j in range(i * 2, 50, i)]
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 10, 15, 20, 25, 30, 35, 40, 45, 12, 18, 24, 30, 36, 42, 48, 14, 21, 28, 35, 42, 49, 16, 24, 32, 40, 48]

# SC를 사용하면 중복값이 없는 집합을 얻을 수 있다
no_primes = {j for i in range(2, 9) for j in range(i * 2, 50, i)}
# {4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49}

# -----------------------------------------------------------------------------------------

""" 3. dict coprehension """
# 두 리스트를 하나의 dict로 합치는 DC. 하나는 key, 또 다른 하나는 value로 사용한다
subjects = ["math", "history", "english", "computer engineering"]
scores = [90, 80, 95, 100]
score_dict = {key: value for key, value in zip(subjects, scores)}
# {'math': 90, 'history': 80, 'english': 95, 'computer engineering': 100}

# 튜플 리스트를 dict 형태로 변환하는 DC
score_tuples = [
    ("math", 90),
    ("history", 80),
    ("english", 95),
    ("computer engineering", 100),
]
score_dict = {t[0]: t[1] for t in score_tuples}
# {'math': 90, 'history': 80, 'english': 95, 'computer engineering': 100}

"""또 다른 예시"""
"""정렬 단계, 18870 좌표 압축"""

# 받을 숫자의 개수
n = int(input())

# 숫자를 리스트의 저장
x = list(map(int, input().split()))

# 리스트 안 중복을 제거하고 오름차순으로 정렬
xt = list(sorted(set(x)))

# 작은 것부터 차례대로 원래 값을 key, 압축된 좌표를 value로 딕셔너리에 저장
xt = {xt[i]: i for i in range(len(xt))}

# 원래 리스트의 값을 딕셔너리 key로 넣어서 value를 출력
# 이때 *을 붙이면 띄어쓰기 형식으로, 안 붙이면 리스트로 출력됨
print(*[xt[i] for i in x])


# -----------------------------------------------------------------------------------------

""" 4. generator expression """
# 다음 Generator는 제곱수를 만들어낸다
gen = (x**2 for x in range(10))
print(gen)
# <generator object <genexpr> at 0x105bde5c8>
print(next(gen))  # call 1
# 0
print(next(gen))  # call 2
# 1
# 'next' 함수 호출을 10번 반복
print(next(gen))  # call 10
# 81
print(next(gen))  # call 11
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""

# Yes, it is an just generator. You can sum the yielding values.
# GE로 생성한 Generator도 yield를 가진 함수로 생성한 것과 동일한 Generator이기 때문에, 똑같이 sum을 사용할 수 있다. (iterable 객체)
gen = (x**2 for x in range(10))
sum_of_squares = sum(gen)
# 285
