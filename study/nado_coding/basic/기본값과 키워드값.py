#기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이: {1}\t주 사용 언어 : {2}" \
#         .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이: {1}\t주 사용 언어 : {2}" \
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# 키워드값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "유재석", main_lang="파이썬", age = 20)
# profile(main_lang="자바", name = "김태호", age = 27)

#가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t" .format(name, age), end = " ") # end = " "는 줄바꿈 안하고 계속 쓰게 만듬
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이: {1}\t" .format(name, age), end = " ") # end = " "는 줄바꿈 안하고 계속 쓰게 만듬
    for lang in language:
        print(lang, end = " ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
profile("김태호", 25, "Kotlin", "Swift")