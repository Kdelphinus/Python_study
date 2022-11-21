def sale_event(n: int, p: int) -> int:
    sp = p
    if n >= 20:
        sp = min(sp, int(p * 0.75))
    if n >= 15:
        sp = min(sp, p - 2000)
    if n >= 10:
        sp = min(sp, int(p * 0.9))
    if n >= 5:
        sp = min(sp, p - 500)
    return 0 if sp < 0 else sp


if __name__ == "__main__":
    num = int(input())
    price = int(input())
    print(sale_event(num, price))
