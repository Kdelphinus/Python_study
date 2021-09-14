from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement


items = ["A", "B", "C", "D"]

"""순열, permutations(반복 가능한 객체, 사용할 원소의 수)"""
# # 모든 원소를 사용하여 순열을 만든다
# print("순열(map과 join으로 붙이지 않으면): ", list(permutations(items)))

# 2개의 원소를 사용하여 순열을 만든다
print("순열: ", list(map("".join, permutations(items, 2))))

# 1 ~ 10까지 담긴 리스트에서 4개의 원소를 이용하여 순열 만들기
P = permutations(range(1, 10 + 1), 4)


"""조합, combinations(반복 가능한 객체, 사용할 원소의 수)"""
# 조합은 무조건 몇개의 원소를 사용할 지 넘겨주어야 한다

# 모든 원소를 사용하여 조합을 만든다
print("조합: ", list(map("".join, combinations(items, len(items)))))

# 2개의 원소를 사용하여 조합을 만든다
print("조합: ", list(map("".join, combinations(items, 2))))

"""조합과 순열의 차이"""
# 순열은 순서가 같은 원소로 만들어져도 순서가 다르게 붙으면 다른 원소로 인식
# 조합은 같은 원소로 만들어진 것은 순서에 관계없이 중복된 값으로 인식


"""중복 순열, product(반복 가능한 객체, repeat=사용할 원소의 수)"""
# 값들을 중복하여 순열을 만든다
print("중복 순열: ", list(map("".join, product(items, repeat=2))))


""" 중복 조합, combinations_with_replacement(반복 가능한 객체, 사용할 원소의 수)"""
# 값들을 중복하여 조합을 만든다
print("중복 조합: ", list(map("".join, combinations_with_replacement(items, 2))))
