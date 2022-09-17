"""2020 KAKAO BLIND RECRUITMENT"""


def solution(s):
    answer = len(s)  # 최대 길이는 아무것도 압축하지 못했을 때
    cnt = len(s)  # 처음은 압축된 것이 없다
    cut = 1  # 글자를 나눌 단위
    num = 1  # 압축한 글자 앞에 붙을 숫자, 자신은 미리 포함하기에 1
    i = 0  # 앞에서부터 확인할 인덱스
    j = i + cut  # 앞에서 구한 문자와 비교할 문자의 인덱스
    flag = False  # 한 번이라도 압축했는지 표시할 플래그

    while cut <= len(s) // 2:  # 압축은 문자열의 절반 단위까지만 가능
        if j + cut > len(s):  # 남은 문자의 압축이 불가능 할 때
            if flag:  # 만약 전에 압축을 했었다면
                cnt += len(str(num))  # 앞에 압축한 문자의 개수를 붙이고
                num = 1  # num 초기화
            cut += 1  # 글자를 나눌 단위를 하나 늘리고
            answer = min(answer, cnt)  # 이미 구한 것과 지금 구한 것 중 작은 값을 저장

            # 각종 값 초기화
            i = 0
            j = i + cut
            cnt = len(s)
            flag = False

        if s[i : i + cut] == s[j : j + cut]:  # 압축이 가능하면
            num += 1  # 같은 문자 개수 하나 추가
            j += cut  # 다음 문자 확인을 위하여 인덱스 이동
            cnt -= cut  # 문자 압축
            flag = True  # 문자 압축 했다고 표시
        else:  # 압축이 불가하면
            if flag:  # 한 번이라도 압축했으면
                cnt += len(str(num))  # 앞에 압축한 문자의 개수를 붙이고
                num = 1  # num 초기화
            i = j  # 압축하지 못한 곳부터 확인 시작
            j = i + cut  # 비교할 대상은 i부터 cut 떨어진 위치
            flag = False  # flag 초기화

    return answer


# test case
a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
    "aaaaaa",
]

print("나의 풀이")
for x in a:
    print(solution(x))


# -----------------------------------------------------------------------------------------------------------------------
# 최다 추천 풀이
def compress(text, tok_len):
    """compress

    Args:
        text (list): 압축할 문자열
        tok_len (int)): 문자를 나눌 단위

    Returns:
        [type]:
    """
    words = [
        text[i : i + tok_len] for i in range(0, len(text), tok_len)
    ]  # tok_len을 기준으로 문장을 나눠 리스트에 저장
    res = []
    cur_word = words[0]  # 첫 기준이 되는 가장 앞 문자
    cur_cnt = 1  # 압축할 문자의 개수
    for a, b in zip(words, words[1:] + [""]):  # 앞 문자와 뒷 문자를 비교
        if a == b:  # 압축이 가능하다면
            cur_cnt += 1  # 압축할 문자 개수 추가
        else:  # 압축이 불가하다면
            res.append([cur_word, cur_cnt])  # 현재 문자와 압축한 개수를 res에 저장
            cur_word = b  # 현재 문자를 변경
            cur_cnt = 1  # 압축할 문자 개수 초기화
    return sum(
        len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res
    )  # 압축이 끝난 문자의 길이


def solution(text):
    """1 ~ text // 2까지 단위를 가지고 나눈 문자의 길이와 압축 전 길이를 저장하여 그 중 가장 작은 값을 리턴하는 함수"""
    return min(
        compress(text, tok_len)
        for tok_len in list(range(1, int(len(text) / 2) + 1))
        + [len(text)]  # 길이가 1인 문자는 compress가 작동하지 않으므로 이를 방지하기 위해 [len(text)]를 삽입
    )


# test case
a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
    "aaaaaa",
]

print("\n최다 추천 풀이")
for x in a:
    print(solution(x))
