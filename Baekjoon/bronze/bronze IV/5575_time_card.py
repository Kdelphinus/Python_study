for _ in range(3):
    ah1, am1, as1, ah2, am2, as2 = map(int, input().split())
    if as2 < as1:
        as2 += 60 - as1
        if am2 == 0:
            am2 = 59
            ah2 -= 1
        else:
            am2 -= 1
    else:
        as2 -= as1
    if am2 < am1:
        am2 += 60 - am1
        ah2 -= 1
    else:
        am2 -= am1
    ah2 -= ah1
    print(f"{ah2} {am2} {as2}")
