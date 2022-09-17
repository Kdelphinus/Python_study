import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# numpy 임의성 조절
np.random.seed(42)

# 데이터 셋을 가져와 입력, 목표 변수로 나누기
dataset = pd.read_csv(
    "codeit/11. (미완)딥 러닝/data/MNIST_preprocessed.csv", sep=",", header=None
).values
X = dataset[:, 0:784]
Y = dataset[:, 784:]

# training, testing set으로 나누기
X_train, X_test = (X[0:250,], X[250:,])
Y_train, Y_test = (Y[0:250,], Y[250:,])


def sigmoid(x):
    """시그모이드 함수"""
    return 1 / (1 + np.exp(-x))


def d_sigmoid(x):
    """시그모이드 미분 함수"""
    return (np.exp(-x)) / ((np.exp(-x) + 1) ** 2)


def initialize_parameters(neurons_per_layer):
    """신경망의 가중치와 편향을 초기화해주는 함수"""
    L = len(neurons_per_layer) - 1  # 입력층을 포함한 층 개수 저장
    parameters = {}

    # 1층부터 L층까지 돌면서 가중치와 편향 초기화
    for l in range(1, L + 1):
        parameters["W" + str(l)] = np.random.randn(
            neurons_per_layer[l], neurons_per_layer[l - 1]
        ) * np.sqrt(1.0 / neurons_per_layer[l])
        parameters["b" + str(l)] = np.random.randn(neurons_per_layer[l]) * np.sqrt(
            1.0 / neurons_per_layer[l]
        )

    return parameters


def feed_forward(x, parameters):
    """순전파 함수"""
    cache = {"a0": x}
    L = len(parameters) // 2  # 가중치와 편향이 같이 저장되므로

    for l in range(1, L + 1):
        # 전 층 뉴런의 출력, 현재 층 뉴런들의 가중치, 편향 데이터를 가지고 온다
        a_prev = cache["a" + str(l - 1)]
        W = parameters["W" + str(l)]
        b = parameters["b" + str(l)]

        # 데이터로 z(순전파의 값)와 a(뉴런의 출력)를 계산한다
        z = W @ a_prev + b
        a = sigmoid(z)

        # 결과 값을 캐쉬에 저장한다
        cache["z" + str(l)] = z
        cache["a" + str(l)] = a

    return a, cache


def compute_accuracy(x_val, y_val, parameters):
    """테스트 데이터에서 예측값들의 성능을 계산하는 함수"""
    predictions = []

    for x, y in zip(x_val, y_val):
        output, _ = feed_forward(x, parameters)
        pred = np.argmax(output)
        predictions.append(pred == np.argmax(y))

    return np.mean(predictions)


def compute_loss(x_val, y_val, parameters):
    """학습 데이터에서 현재 모델의 손실을 계산하는 함수"""
    loss = 0

    for x, y in zip(x_val, y_val):
        output, _ = feed_forward(x, parameters)
        loss += np.mean((output - y) ** 2) / 2

    return loss / len(x_val)


def back_prop(prediction, y, cache, parameters):
    """역전파 함수"""
    gradients = {}
    L = len(cache) // 2
    da = (prediction - y) / y.shape[0]

    for layer in range(L, 0, -1):
        # 편미분 계산에 필요한 데이터 가지고 오기
        a_prev = cache["a" + str(layer - 1)]
        z = cache["z" + str(layer)]
        W = parameters["W" + str(layer)]

        # 역전파 행렬 연산을 사용해서 각 요소에 대한 편미분 계산
        db = d_sigmoid(z) * da
        dW = np.outer(db, a_prev)
        da = W.T @ db

        # 계산한 편미분 값들을 저장
        gradients["dW" + str(layer)] = dW
        gradients["db" + str(layer)] = db

    # 계산한 편미분 값들을 리턴
    return gradients


def update(parameters, gradients, alpha, m):
    """계산한 경사로 가중치와 편향을 업데이트 하는 함수"""
    L = len(parameters) // 2

    for layer in range(1, L + 1):
        parameters["W" + str(layer)] -= alpha * gradients["dW" + str(layer)] / m
        parameters["b" + str(layer)] -= alpha * gradients["db" + str(layer)] / m

    return parameters


def train_nn(X_train, Y_train, X_test, Y_test, neurons_per_layer, epoch, alpha):
    """신경망을 학습시키는 함수"""
    parameters = initialize_parameters(neurons_per_layer)
    loss_list = []
    m = X_train.shape[0]

    # epoch번 경사 하강을 한다
    for i in range(epoch):
        parameters_copy = parameters.copy()

        # 모든 이미지에 대해서 경사 계산 후, 평균 계산
        for x, y in zip(X_train, Y_train):
            prediction, cache = feed_forward(x, parameters)
            gradients = back_prop(prediction, y, cache, parameters)
            parameters_copy = update(parameters_copy, gradients, alpha, m)

        # 가중치와 편향을 실제로 업데이트
        parameters = parameters_copy
        loss_list.append(compute_loss(X_train, Y_train, parameters))
        print(
            "{}번째 경사 하강, 테스트 셋에서 성능: {}".format(
                i + 1, round(compute_accuracy(X_test, Y_test, parameters), 2)
            )
        )

    return loss_list, parameters


# 실행 코드
neurons_per_layer = [784, 128, 64, 10]
parameters = initialize_parameters(neurons_per_layer)

loss_list, parameters = train_nn(
    X_train, Y_train, X_test, Y_test, neurons_per_layer, 25, 300
)

# 디버깅을 위한 시각화 코드
plt.plot(loss_list)
print(plt.show())
