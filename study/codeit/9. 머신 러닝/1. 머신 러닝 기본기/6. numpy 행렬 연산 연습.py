import numpy as np

A = np.array([[1, -1, 2], [3, 2, 2]])

B = np.array([[0, 1], [-1, 1], [5, 2]])

C = np.array([[2, -1], [-3, 3]])

D = np.array([[-5, 1], [2, 0]])

# 행렬 연산 결과를 result에 저장하세요
result = 2 * A @ (-B) @ (3 * C + D)

print(result)
