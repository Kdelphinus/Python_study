def survival_classifier(seat_belt, highway, speed, age):
    """조건들을 보고 생존은 0, 사망은 1을 리턴하는 함수"""

    if seat_belt:  # 안전벨트를 했는가
        return 0
    else:
        if highway:  # 고속도로인가
            if speed > 100:  # 시속 100km/h가 넘었는가
                if age > 50:  # 나이가 50살이 넘었는가
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0


print(survival_classifier(False, True, 110, 55))
print(survival_classifier(True, False, 40, 70))
print(survival_classifier(False, True, 80, 25))
print(survival_classifier(False, True, 120, 60))
print(survival_classifier(True, False, 30, 20))