# Quiz) 신조어 퀴즈 클래스를 만드시오.

# - word 클래스 작성
# __init__(...) : 신조어, 보기1, 보기2, 정답을 받아서 멤버 변수 설정
# show_question(...) : 질문 내용 표시
# check_answer(...) : 입력값이 정답인지 확인하여 "정답입니다." 또는 "틀렸습니다." 출력

# - 주어진 프로그램 예제
# word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부",1)
# word.show_question()
# word.check_answer(int(input("=>")))

# - 출력 결과
# "얼죽아"의 뜻은?
# 1. 얼어 죽어도 아메리카노
# 2. 얼굴만은 죽어도 아기피부
# =>

class Word:
    def __init__(self, question, example1, example2, answer):
        self.question = question
        self.example1 = example1
        self.example2 = example2
        self.answer = answer
    
    def show_question(self):
        print('"{}"의 뜻은?'.format(self.question))
        print("1." + self.example1)
        print("2." + self.example2)
    
    def check_answer(self, user_input):
        if user_input == self.answer:
            print("정답입니다.")
        else:
            print("틀렸습니다.")

word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부",1)
word.show_question()
word.check_answer(int(input("=>")))