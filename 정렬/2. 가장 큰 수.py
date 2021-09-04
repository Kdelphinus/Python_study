"""해답"""
# 링크: https://jokerldg.github.io/algorithm/2021/05/06/most-big-number.html
def solution(numbers):
    answer = ""
    numbers = list(map(str, numbers))
    """
    Q) x: x * 3?
    -> 각각의 문자열을 3번 반복하여 정렬한다는 의미
    -> numbers 안에 들어있는 숫자가 1000 이하이므로 3자리수로 맞춘 후 비교하는 것
        ex) ["6", "2", "21", "23", "10"] (내림차순 정렬한다고 했을 때)
            1. x * 3을 했기에 ["666", "222", "212121", "232323", "101010"]을 기준으로 정렬
            2. 문자열이기에 첫번째 인덱스부터 아스키코드를 기준으로 정렬
            3. "6"이 가장 크므로 맨 앞
            4. "2"가 동률인 세 개의 값은 두번째 인덱스도 비교한다
            5. 두번째 인덱스를 기준으로 "23", "2", "21"로 정렬된다
            6. 마지막으로 "10"이 정렬된다

    Q) 1000이하를 x * 3으로 해야하는 이유?
    -> ["9", "991"]에다가 x * 2를 하면 ["99", "991991"]이다
    -> 이는 여전히 "991"이 더 큰 값으로 인식된다
    -> 그렇기에 최소 x * 3은 해야한다
    """
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(numbers)))


print(solution([6, 2, 10]))  # "6210"
print(solution([3, 30, 34, 5, 9]))  # "9534330"


# ----------------------------------------------------------------------------------------------
"""시간 초과"""
from itertools import permutations


def solution(numbers):
    answer = ""
    numbers = [str(i) for i in numbers]
    nums = list(map("".join, permutations(numbers, len(numbers))))
    nums.sort()

    return nums[-1]
