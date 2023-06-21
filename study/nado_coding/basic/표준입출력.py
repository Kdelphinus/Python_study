# print("Python", "Java", "Javascript", sep =",", end="?")
# # sep로 출력 형태를 지정할 수 있음, end는 끝부분을 지정할 수 있음
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file = sys.stdout)
# print("Python", "Java", file = sys.stderr)

# 시험성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001,002,003...

# for num in range(1, 21):
#     print("대기번호: " + str(num).zfill(3)) #zfill(3)은 3자리를 채우고 빈공간은 0으로 채움

answer = input("아무 값이나 입력하세요 : ")  # input은 숫자든 문자든 항상 문자열 형태
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")
