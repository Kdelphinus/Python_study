def seven_dwarf():
    dwarfs = []
    for _ in range(9):
        dwarfs.append(int(input()))
    fake = sum(dwarfs) - 100

    for i in range(8):
        for j in range(i + 1, 9):
            if fake == dwarfs[i] + dwarfs[j]:
                del dwarfs[j]
                del dwarfs[i]
                return dwarfs


def main():
    dwarf = seven_dwarf()
    for d in dwarf:
        print(d)


if __name__ == "__main__":
    main()
