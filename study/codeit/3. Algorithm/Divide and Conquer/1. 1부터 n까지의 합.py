def consecutive_sum(start, end):
    if start == end:
        return start
    num = int((start + end) / 2)
    return consecutive_sum(start, num) + consecutive_sum(num + 1, end)

print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))