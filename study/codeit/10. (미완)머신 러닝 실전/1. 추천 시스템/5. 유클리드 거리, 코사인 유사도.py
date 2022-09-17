import numpy as np
from math import sqrt


def distance(user_1, user_2):
    """유클리드 거리를 계산해주는 함수"""
    return sqrt(np.sum((user_1 - user_2) ** 2))


def cosine(user_1, user_2):
    """코사인 유사도를 계산해주는 함수"""
    return user_1.T @ user_2 / (sqrt(np.sum(user_1 ** 2)) * sqrt(np.sum(user_2 ** 2)))


user_1 = np.array([0, 1, 2, 3, 4, 5])
user_2 = np.array([0, 1, 4, 6, 1, 4])

print("유클리드 거리: ", distance(user_1, user_2))
print("코사인 유사도: ", cosine(user_1, user_2))