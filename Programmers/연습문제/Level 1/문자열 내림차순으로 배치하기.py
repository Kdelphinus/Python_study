def solution(s):
    anw = ""
    tmp = []

    for i in s:  # 주어진 문자열들을 아스키코드로 변환
        tmp.append(ord(i))
    tmp.sort(key=lambda x: -x)  # 내림차순으로 정렬
    # 대문자는 아스키코드가 소문자보다 작다

    for i in tmp:  # 다시 문자열로 바꾸어 anw에 저장
        anw += chr(i)

    return anw
