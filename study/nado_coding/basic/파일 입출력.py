# 파일 만들기
# score_file = open("score.txt", "w", encoding="utf8") # w는 쓰는 것, utf8은 한글을 위해
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close()

# 파일에 내용 추가하기
# score_file = open("score.txt", "a", encoding='utf8')
# score_file.write("코딩 : 100")
# score_file.write("\n과학 : 80")
# score_file.close()

# 모든 내용 불러오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# 한 줄씩 불러오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# 파일이 몇 줄인 줄 모를 때 모든 줄 불러오기
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# 리스트 이용
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
