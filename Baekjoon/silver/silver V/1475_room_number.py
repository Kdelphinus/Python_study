import sys
from collections import Counter


INPUT = sys.stdin.readline


def set_cnt(nums: str) -> int:
    nums = Counter(nums)
    tmp = (
        (nums["9"] + nums["6"]) // 2 + 1
        if (nums["9"] + nums["6"]) % 2
        else (nums["9"] + nums["6"]) // 2
    )
    nums["6"] = nums["9"] = tmp
    return nums.most_common()[0][1]


if __name__ == "__main__":
    numbers = INPUT().strip()
    print(set_cnt(numbers))
