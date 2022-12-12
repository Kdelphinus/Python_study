# 문제 설명이 아주 이해하기 어렵다. 뭔소리야...
# 링크: https://pacific-ocean.tistory.com/105


def make_stick(goal: int) -> int:
    return bin(goal).count("1")


if __name__ == "__main__":
    print(make_stick(int(input())))
