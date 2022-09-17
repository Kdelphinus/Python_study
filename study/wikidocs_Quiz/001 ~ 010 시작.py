# 001 Hello World 출력
print("Hello World")

# 002 Mary's cosmetics 출력
print("Mary's cosmetics")

# 003 신씨가 소리질렀다. "도둑이야". 를 출력
print('신씨가 소리질렀다. "도둑이야".')

# 004 "C:\Windows" 출력
print('"C:\windows"')

# 005 print("안녕하세요.\n만나서\t\t반갑습니다.") 를 출력하고 \n과 \t의 역할?
# print("안녕하세요.\n만나서\t\t반갑습니다.")
# \n : 줄바꿈, \t : tab 역할

# 006 print("오늘은", "일요일") 을 출력할 때 예상되는 결과는?
# 오늘은 일요일 이라고 출력될 것
# print 문에서 ,는 뛰어쓰기 포함

# 007 naver;kakao;sk;samsung 을 출력할 것
print("naver", "kakao", "sk", "samsung", sep=";") 
# sep을 이용하면 공백대신 다른 문자를 입력할 수 있음

# 008 naver/kakao/sk/samsung 을 출력할 것
print("naver", "kakao", "sk", "samsung", sep="/")

# 009 print("first");print("second") 를 줄바꿈 없이 출력하도록 수정
# ;은 한줄에 여러 개의 명령을 작성하기 위해 사용함
print("first", end="");print("second")

# 010 5/3의 결과를 화면에 출력
print(5/3)