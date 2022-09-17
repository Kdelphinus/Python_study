def solution(nums):
    nums_divide = len(nums) / 2  # 가져가야 할 개수
    nums = set(nums)  # 종류만 남김
    sort = len(nums)  # 다른 종류의 수

    if sort >= nums_divide:  # 종류가 가져가야 할 수보다 같거나 많으면
        return nums_divide  # 각각 다른 종류로 가져가면 됨
    else:  # 종류가 가져가야 할 수보다 작다면
        return sort  # 종류별로 하나씩 택하고 중복되는 것을 가져감


print(solution([3, 1, 2, 3]))
