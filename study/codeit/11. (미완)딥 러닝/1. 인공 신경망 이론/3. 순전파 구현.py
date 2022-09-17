import numpy as np
import pandas as pd

# numpy 임의성 조절
np.random.seed(42)

# 데이터 셋을 가져와 입력, 목표 변수로 나누기
dataset = pd.read_csv(
    "codeit/11. (미완)딥 러닝/data/MNIST_preprocessed.csv", sep=",", header=None
).values
X = dataset[:, 0:784]
Y = dataset[:, 784:]

# training, testing set으로 나누기
X_train, X_test = (
    X[0:250,],
    X[250:,],
)
Y_train, Y_test = (
    Y[0:250,],
    Y[250:,],
)


def sigmoid(x):
    """시그모이드 함수"""
    return 1 / (1 + np.exp(-x))


def initialize_parameters(nodes_per_layer):
    """신경망의 가중치와 편향을 초기화해주는 함수"""
    L = len(nodes_per_layer) - 1  # 층 개수 저장
    parameters = {}

    # 1층부터 L층까지 돌면서 가중치와 편향 초기화
    for l in range(1, L + 1):
        parameters["W" + str(l)] = np.random.randn(
            nodes_per_layer[l], nodes_per_layer[l - 1]
        ) * np.sqrt(1.0 / nodes_per_layer[l])
        parameters["b" + str(l)] = np.random.randn(nodes_per_layer[l]) * np.sqrt(
            1.0 / nodes_per_layer[l]
        )

    return parameters


def feed_forward(x, parameters):
    """순전파 함수"""
    cache = {"a0": x}  # 0번째 층 출력 저장
    L = len(parameters) // 2  # 층 수 저장

    for l in range(1, L + 1):
        # 전 층 뉴런의 출력, 현재 층 뉴런들의 가중치, 편향 데이터를 가지고 온다
        a_prev = cache["a" + str(l - 1)]
        W = parameters["W" + str(l)]
        b = parameters["b" + str(l)]

        # 가지고 온 데이터로 z(뉴런의 출력)와 a(층의 출력)를 계산한다
        z = W @ a_prev + b
        a = sigmoid(z)

        # 결과값을 캐시에 저장한다
        cache["z" + str(l)] = z
        cache["a" + str(l)] = a

    return a, cache


neurons_per_layer = [784, 128, 64, 10]
parameters = initialize_parameters(neurons_per_layer)
print(feed_forward(X_train[0], parameters)[0])  # a와 cache 중 a만 출력하기 위해 마지막에 [0]을 씀
