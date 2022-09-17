from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)

    while True:
        price = prices.popleft()  # 가장 앞 가격을 빼준 후 price에 저장
        second = 0

        for other in prices:  # 그 후, 가격들과 비교
            second += 1  # 떨어지기 전까지 시간을 계속 더함
            if price > other:  # 가격이 떨어지면 반복문 종료
                break

        if not prices:  # 마지막 가격일 때
            answer.append(0)
            break

        answer.append(second)

    return answer


# 테스트 코드
prices = [1, 2, 3, 2, 3]
print(solution(prices))