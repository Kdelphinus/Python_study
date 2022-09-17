"""2018 KAKAO BLIND RECRUITMENT"""


def solution(files):
    files_hnt = []
    for idx, file in enumerate(files):
        flag = False
        temp = []
        for i in range(len(file)):
            if not flag and file[i].isdigit():  # head부분
                flag = True
                temp.append(file[:i])
                start = i
            if flag and not file[i].isdigit():  # tail이 있을 때
                temp.append(file[start:i])  # num부분
                temp.append(file[i:])  # tail부분
                temp.append(idx)  # 원래 위치
                break
            if flag and i == len(file) - 1:  # tail이 없을 때
                temp.append(file[start:])  # num부분
                temp.append("")  # tail은 없다
                temp.append(idx)  # 원래 위치
                break
        files_hnt.append(temp)

    # head(대소문자 구분 안함), num, 원래 위치 순으로 오름차순
    files_hnt.sort(key=lambda x: (x[0].lower(), int(x[1]), x[3]))

    # 원래 위치를 제외하고 다시 붙여서 출력
    return ["".join(file[:-1]) for file in files_hnt]


print(solution(["ab52", "cd65"]))  # ["ab52", "cd65"]
print(
    solution(
        ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    )
)  # ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(
    solution(
        [
            "F-5 Freedom Fighter",
            "B-50 Superfortress",
            "A-10 Thunderbolt II",
            "F-14 Tomcat",
        ]
    )
)  # ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

# -----------------------------------------------------------------------------------------------

"""정규식 사용한 해답"""
import re


def solution(files):
    a = sorted(files, key=lambda file: int(re.findall("\d{1,5}", file)[0]))
    b = sorted(a, key=lambda file: re.split("\d{1,5}", file.lower())[0])
    return b
