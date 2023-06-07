def vertical_reading(strings: list) -> str:
    max_len, vr = 0, ""
    for string in strings:
        max_len = max(max_len, len(string))
    for j in range(max_len):
        for i in range(5):
            if len(strings[i]) > j:
                vr += strings[i][j]
    return vr


if __name__ == "__main__":
    STRINGS = [input() for _ in range(5)]
    print(vertical_reading(STRINGS))
