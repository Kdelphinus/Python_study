import numpy as np


"""np.sum, np.mean, np.nansum, np.nanmean"""

A = np.array(
    [
        [3, 3, 2, 3, 1],
        [5, 2, 2, 3, 1],
        [3, 3, 2, 3, 1],
        [3, 1, 4, 3, 1],
    ]
)

# 모든 요소들의 합과 평균
print(np.sum(A))  # 49
print(np.mean(A))  # 2.45

B = np.array(
    [
        [3, 3, 2, 3, 1],
        [5, 2, 2, 3, 1],
        [3, np.nan, 2, 3, 1],
        [3, 1, 4, 3, 1],
    ]
)

# nan이 하나라도 있으면 nan을 리턴
print(np.sum(B))  # nan
print(np.mean(B))  # nan

# nan을 제외한 나머지 값들의 합과 평균
print(np.nansum(B))  # 46.0
print(np.nanmean(B))  # 2.421...


"""데이터 접근"""
A = np.array(
    [
        [3, 3, 2, 3, 1],
        [5, 2, 2, 3, 1],
        [3, 3, 2, 3, 1],
        [3, 1, 4, 3, 1],
    ]
)

# 행 접근법
print(A[0])  # array([3, 3, 2, 3, 1])
print(A[2][2])  # 2

# 열 접근법
print(A[:, 3])  # array([3, 3, 3, 3])
print(A[:, 0])  # array([3, 5, 3, 3])
print(A[3, :])  # array([3, 1, 4, 3, 1])  == A[3]


"""원하는 차원의 행렬을 임의로 생성"""
random_matrix = np.random.rand(3, 5)  # 3 x 5 행렬을 임의로 생성

"""numpy에서 임의성 도구들의 결과가 일정하게 나오도록 해줌"""
np.random.seed(5)
