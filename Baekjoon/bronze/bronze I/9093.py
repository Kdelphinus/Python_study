def reverse_str(string: str) -> None:
    for s in string.split():
        print(s[::-1], end=" ")
    print()


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        STRING = input()
        reverse_str(STRING)
