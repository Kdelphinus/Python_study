def convert_cpp_to_java(name: str) -> str:
    convert = ""
    name = list(name.split("_"))

    try:
        for i, n in enumerate(name):
            if not n:
                raise ValueError
            for c in n:
                if c.isupper():
                    raise ValueError
            if i == 0:
                convert += n
                continue
            convert += n[0].upper()
            if len(n) > 1:
                convert += n[1:]
    except ValueError:
        return "Error!"

    return convert


def convert_java_to_cpp(name: str) -> str:
    if name[0].isupper():
        return "Error!"
    convert = name[0]

    try:
        for i, n in enumerate(name):
            if i == 0:
                continue

            convert += "_" + n.lower() if n.isupper() else n
    except ValueError:
        return "Error!"

    return convert


def convert_name(name: str) -> str:
    if not name or name[0] == "_" or name[-1] == "_":
        return "Error!"

    return convert_cpp_to_java(name) if "_" in name else convert_java_to_cpp(name)


if __name__ == "__main__":
    ORIGIN = input()
    CONVERT = convert_name(ORIGIN)
    print(CONVERT)
