def is_FA(num: str) -> str:
    tmp = ""
    while len(tmp) < len(num):
        tmp = str(int(num[0]) * len(num))
        if len(num) >= len(tmp):
            return "FA"
        num = tmp
    return "NFA"


if __name__ == "__main__":
    print(is_FA(input()))
