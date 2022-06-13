import random

with open("codeit/basic_of_python/vocabulary.txt", "r", encoding = "utf8") as voca:
    eng = []
    kor = []
    for line in voca:
        word = line.strip().split(": ")
        eng.append(word[0])
        kor.append(word[1])
    while True:
        i = random.randint(0, len(kor)-1)

        anw = input(f"{kor[i]}: ")
        if anw == eng[i]:
            print("맞았습니다!")
        elif anw == "q":
            break
        else:
            print(f"아쉽습니다. 정답은 {eng[i]}입니다.")
