def recreate_word(word: str) -> str:
    ans = ""
    for i in range(1, len(word) - 1):
        for j in range(i + 1, len(word)):
            tmp = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]
            ans = tmp if ans == "" else min(tmp, ans)
    return ans


if __name__ == "__main__":
    print(recreate_word(input()))
