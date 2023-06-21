def find_factors(num: int):
    factors = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    return sorted(factors)


def main():
    num = int(input())
    while num != -1:
        factors = find_factors(num)
        if sum(factors) == num:
            print(f"{num} = ", end="")
            for idx, factor in enumerate(factors):
                if idx < len(factors) - 1:
                    print(f"{factor} + ", end="")
                else:
                    print(factor)
        else:
            print(f"{num} is NOT perfect.")
        num = int(input())


if __name__ == "__main__":
    main()
