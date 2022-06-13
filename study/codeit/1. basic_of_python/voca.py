with open("codeit/basic_of_python/vocabulary.txt", "a", encoding = "utf8") as voca:
    while True:
        eng = input("영어 단어를 입력하세요: ")
        if eng == "q":
            break
        kor = input("한국어 뜻을 입력하세요: ")
        if kor == "q":
            break
        voca.write(f"{eng}: {kor}\n")