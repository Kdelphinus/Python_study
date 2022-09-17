"""나의 풀이"""


def solution(answers):
    answer_1 = []
    answer_2 = []
    answer_3 = []

    cnt = 0
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0

    # 1번 학생의 답
    for i in range(len(answers)):
        answer_1.append(i % 5 + 1)

    # 2번 학생의 답
    for i in range(len(answers)):
        if i % 2 != 0:
            cnt += 1
            if cnt == 2:
                cnt += 1
                answer_2.append(cnt)
            elif cnt == 5:
                answer_2.append(cnt)
                cnt = 0
            else:
                answer_2.append(cnt)
        else:
            answer_2.append(2)

    # 3반 학생의 답
    for i in range(len(answers)):
        if i % 10 <= 1:
            answer_3.append(3)
        elif i % 10 <= 3:
            answer_3.append(1)
        elif i % 10 <= 5:
            answer_3.append(2)
        elif i % 10 <= 7:
            answer_3.append(4)
        else:
            answer_3.append(5)

    # 채점
    for i in range(len(answers)):
        if answers[i] == answer_1[i]:
            cnt_1 += 1
        if answers[i] == answer_2[i]:
            cnt_2 += 1
        if answers[i] == answer_3[i]:
            cnt_3 += 1

    # 출력
    if cnt_1 > cnt_2 and cnt_1 > cnt_3:
        return [1]
    elif cnt_2 > cnt_1 and cnt_2 > cnt_3:
        return [2]
    elif cnt_3 > cnt_2 and cnt_3 > cnt_1:
        return [3]
    elif cnt_1 == cnt_2 and cnt_1 > cnt_3:
        return [1, 2]
    elif cnt_1 == cnt_3 and cnt_1 > cnt_2:
        return [1, 3]
    elif cnt_3 == cnt_2 and cnt_2 > cnt_1:
        return [2, 3]
    else:
        return [1, 2, 3]


"""모범 답안"""


def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    # enumerate는 배열의 인덱스와 값을 리턴한다
    for idx, answer in enumerate(answers):
        print(f"idx = {idx}, answer = {answer}")
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)

    return result


answers = [1, 5, 3, 1, 2, 3, 5, 2, 4, 1]
solution(answers)