from random import randint


def generate_numbers(n):
    num = []
    cnt = 0
    while True:
        i = randint(1, 45)
        if i in num:
            continue
        else:
            num.append(i)
            cnt += 1
        if cnt == n:
            break
        
    return num


def draw_winning_numbers():
    win_num = generate_numbers(7)
    return sorted(win_num[:6]) + win_num[6:] 
        
    return num


def count_matching_numbers(numbers, winning_numbers):
    cnt = 0
    for i in range(len(numbers)):
        if numbers[i] in winning_numbers:
            cnt += 1
    return cnt


def check(numbers, winning_numbers):
    winning_number_1 = winning_numbers[:6]
    bonus = winning_numbers[6]
    cnt = count_matching_numbers(numbers, winning_number_1)
    reward = 0
    if cnt == 6:
        reward = 1000000000
    elif cnt == 5 and bonus in numbers:
        reward = 50000000
    elif cnt == 5:
        reward = 1000000
    elif cnt == 4:
        reward = 50000
    elif cnt == 3:
        reward = 5000
    else:
        reward = 0
    return reward