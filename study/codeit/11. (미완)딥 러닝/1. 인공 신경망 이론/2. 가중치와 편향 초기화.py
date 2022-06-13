import numpy as np

# numpy 임의성 조절
np.random.seed(42)


def initialize_parameters(neurons_per_layer):
    """신경망의 가중치와 편향을 초기화해주는 함수"""
    L = len(neurons_per_layer) - 1  # 층 개수 저장
    parameters = {}

    # 1층부터 L층까지 돌면서 가중치와 편향 초기화(randn은 평균 0, 표준 오차 1인 임의의 행렬 생성)
    # 신경망의 가중치와 편향의 값들을 초기화할 때는, 값들의 표준 오차를 1대신 그 층의 뉴런 개수의 제곱근과 반비례한 값을 사용(더 빠르게 정확하게 학습되기 때문)
    for l in range(1, L + 1):
        parameters["W" + str(l)] = np.random.randn(
            neurons_per_layer[l], neurons_per_layer[l - 1]
        ) * np.sqrt(1 / neurons_per_layer[l])
        parameters["b" + str(l)] = np.random.randn(neurons_per_layer[l]) * np.sqrt(
            1 / neurons_per_layer[l]
        )

    return parameters


neurons_per_layer = [10, 5, 5, 3]
print(initialize_parameters(neurons_per_layer))
