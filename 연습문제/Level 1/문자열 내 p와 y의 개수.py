def solution(s):
    s = s.lower()  # 모두 소문자로 만듬

    p_cnt = s.count("p")  # p의 개수
    y_cnt = s.count("y")  # y의 개수

    if p_cnt == y_cnt:
        return True
    else:
        return False
