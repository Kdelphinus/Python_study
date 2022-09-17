# def solution(s):
#    answer = ""
#    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#    number_dict = {
#        "zero": "0",
#        "one": "1",
#        "two": "2",
#        "three": "3",
#        "four": "4",
#        "five": "5",
#        "six": "6",
#        "seven": "7",
#        "eight": "8",
#        "nine": "9",
#    }

#    i = 0
#    tmp = ""
#    while i < len(s):
#        if s[i] in numbers:
#            answer += s[i]
#        else:
#            tmp += s[i]
#        i += 1
#        if tmp in number_dict.keys():
#            answer += number_dict[tmp]
#            tmp = ""

#    answer += tmp

#    return int(answer)


# print(solution("one4seveneight"))


"""모범답안"""

num_dic = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)  # answer안에 있는 key를 value로 대체
    return int(answer)


print(solution("one4seveneight"))
