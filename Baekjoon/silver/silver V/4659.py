def is_good_pwd(pwd: str) -> bool:
    stack = list(pwd)
    vowel = ["a", "e", "i", "o", "u"]
    past_c, vowel_flag = "", False
    consonant_cnt, vowel_cnt = 0, 0
    while stack:
        c = stack.pop()
        if past_c == c and c != "e" and c != "o":
            return False

        if c in vowel:
            if not vowel_flag:
                vowel_flag = True
            vowel_cnt += 1
            consonant_cnt = 0
        else:
            consonant_cnt += 1
            vowel_cnt = 0
        if vowel_cnt >= 3 or consonant_cnt >= 3:
            return False

        past_c = c

    return True if vowel_flag else False


if __name__ == "__main__":
    while True:
        pwd = input()
        if pwd == "end":
            break
        flag = ""
        if not is_good_pwd(pwd):
            flag = " not"
        print(f"<{pwd}> is{flag} acceptable.")
