def solution(s):
    try:
        int(s)  # 숫자변환이 안되면 문자열이 있는 것
        if len(s) == 4 or len(s) == 6:  # 길이가 4나 6일때만
            return True
        return False
    except:  # 에러가 뜰 때
        return False
