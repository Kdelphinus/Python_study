num = int(input())
mirror = {
    "b": "d",
    "d": "b",
    "i": "i",
    "l": "l",
    "m": "m",
    "n": "n",
    "o": "o",
    "p": "q",
    "q": "p",
    "s": "z",
    "z": "s",
    "u": "u",
    "v": "v",
    "w": "w",
    "x": "x",
}
for i in range(num):
    word = input()
    word_list = list(word.strip())
    copy = ""

    for w in word_list[::-1]:
        if w not in mirror:
            break
        copy += mirror[w]

    if copy == word:
        print("Mirror")
    else:
        print("Normal")
