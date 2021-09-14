# 못 풀었음
# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    stairs_table = [1, 1]

    for height in range(2, stairs + 1):
        stairs_table.append(0)

        for step in possible_steps:
            if height - step >= 0:
                stairs_table[height] += stairs_table[height - step]

    return stairs_table[stairs]


print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))