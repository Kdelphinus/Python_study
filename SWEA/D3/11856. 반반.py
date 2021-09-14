test = int(input())

for t in range(test):
    string = input()
    alpha = [0] * 26

    for i in string:
        alpha[ord(i) - 65] += 1

    alpha = list(set(alpha))

    if sum(alpha) == 2:
        print("#{} Yes".format(t + 1))
    else:
        print("#{} No".format(t + 1))
