from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    cnt = 1
    while len(new_guess) < 3:
        num = int(input(f"{cnt}번째 숫자를 입력하세요: "))
        if 0 > num or 9 < num:
            print("범위를 벗어난 숫자입니다. 다시 입력하세요.")
        elif num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(num)
            cnt += 1 
    
    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(len(guess)):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count


ANSWER = generate_numbers()
tries = 0

while True:
    guess = take_guess()
    S, B = get_score(guess, ANSWER)
    tries += 1
    print(f"{S}S {B}B")
    if S == 3:
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))