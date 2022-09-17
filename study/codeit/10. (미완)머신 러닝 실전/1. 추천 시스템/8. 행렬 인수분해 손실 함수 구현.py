import numpy as np


def cost(prediction, R):
    """행렬 인수분해 알고리즘의 손실을 계산해주는 함수"""
    return np.nansum((prediction - R) ** 2)


# 예측 값 행렬
prediction = np.array(
    [
        [4, 4, 1, 1, 2, 2],
        [4, 4, 3, 1, 5, 5],
        [2, 2, 1, 1, 3, 4],
        [1, 3, 1, 4, 2, 2],
        [1, 2, 4, 1, 2, 5],
    ]
)

# 실제 값 행렬
R = np.array(
    [
        [3, 4, 1, np.nan, 1, 2],
        [4, 4, 3, np.nan, 5, 3],
        [2, 3, np.nan, 1, 3, 4],
        [1, 3, 2, 4, 2, 2],
        [1, 2, np.nan, 2, 2, 4],
    ]
)

print(cost(prediction, R))