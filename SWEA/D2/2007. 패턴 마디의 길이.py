test = int(input())

for t in range(test):
    string = input()
    first = string[0]
    cnt = 0

    for i in range(1, len(string)):
        if first == string[i]:  # 같은 문자열이 나오면
            for j in range(1, i + 1):  # 첫 문자열들과 그 문자열들을 비교
                if string[j] != string[i + j]:  # 다르다면 아님
                    break
                else:  # 맞으면 문자열 길이 추가
                    cnt += 1
        if cnt > 0:
            print("#{} {}".format(t + 1, cnt))
            break