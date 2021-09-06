def solution(s):
    if s[0].isdigit():  # 부호가 없다면
        return int(s)
    else:  # 부호가 있다면
        if s[0] == "+":
            return int(s[1:])
        else:
            return -int(s[1:])
