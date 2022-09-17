test = int(input())

for t in range(test):
    scores_table = [0] * 101
    test_case = int(input())
    scores = list(map(int, input().split()))

    for score in scores:
        scores_table[score] += 1
    result_score = max(scores_table)

    for i in range(100, -1, -1):
        if scores_table[i] == result_score:
            print("#{} {}".format(test_case, i))