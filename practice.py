from itertools import permutations

n, k = 3, 5
person = [i for i in range(1, n + 1)]
print(person)
print(list(map("".join, permutations(person, k))))