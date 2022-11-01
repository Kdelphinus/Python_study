from collections import Counter


def vowel_count(string: str) -> int:
    cnt = Counter(string.lower())
    return cnt["a"] + cnt["e"] + cnt["i"] + cnt["o"] + cnt["u"]


if __name__ == "__main__":
    while True:
        sentence = input()
        if sentence == "#":
            break
        print(vowel_count(sentence))
