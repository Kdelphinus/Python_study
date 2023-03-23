grade = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}


def rating() -> float:
    cnt, total = 0, 0
    for _ in range(20):
        subject, credit, rate = input().split()
        if rate != "P":
            total += float(credit) * grade[rate]
            cnt += float(credit)
    return total / cnt


if __name__ == "__main__":
    print(rating())
