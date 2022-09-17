import numpy as np


def prediction(theta_0, theta_1, x):
    """가설 함수, 주어진 학습 데이터 벡터 x에 대해서 예측 값을 리턴하는 함수"""
    return theta_0 + theta_1 * x


def prediction_difference(theta_0, theta_1, x, y):
    """예측 오차, 모든 예측 값들과 목표 변수들의 오차를 벡터로 리턴해주는 함수"""
    return prediction(theta_0, theta_1, x) - y


def gradient_descent(theta_0, theta_1, x, y, iterations, alpha):
    """경사 하강법, 주어진 theta_0, theta_1 변수들을 경사 하강를 하면서 업데이트 해주는 함수"""
    for _ in range(iterations):  # 정해진 번만큼 경사 하강을 한다
        error = prediction_difference(theta_0, theta_1, x, y)  # 예측값들과 입력 변수들의 오차를 계산

        theta_0 -= alpha * error.mean()
        theta_1 -= alpha * (error * x).mean()

    return theta_0, theta_1


# 입력 변수(집 크기) 초기화 (모든 집 평수 데이터를 1/10 크기로 줄임)
house_size = np.array(
    [0.9, 1.4, 2, 2.1, 2.6, 3.3, 3.35, 3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9]
)

# 목표 변수(집 가격) 초기화 (모든 집 값 데이터를 1/10 크기로 줄임)
house_price = np.array(
    [0.3, 0.75, 0.45, 1.1, 1.45, 0.9, 1.8, 0.9, 1.5, 2.2, 1.75, 2.3, 2.49, 2.6]
)

# theta 값들 초기화 (아무 값이나 시작함)
theta_0 = 2.5
theta_1 = 0

# 학습률 0.1로 200번 경사 하강
theta_0, theta_1 = gradient_descent(theta_0, theta_1, house_size, house_price, 200, 0.1)

print(theta_0, theta_1)