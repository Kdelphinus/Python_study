class Counter:
    """
    시계 클래스의 시,분,초를 각각 나타내는데 사용될 카운터 클래스
    """

    def __init__(self, limit):
        """
        인스턴스 변수 limit(최댓값), value(현재까지 카운트한 값)을 설정한다.
        인스턴스를 생성할 때 인스턴스 변수 limit만 파라미터로 받고, value는 초깃값 0으로 설정한다.
        """
        self.limit = limit
        self.value = 0

    def set(self, new_value):
        """
        파라미터가 0 이상, 최댓값 미만이면 value에 설정한다.
        아닐 경우 value에 0을 설정한다.
        """
        if 0 <= new_value < self.limit:
            self.value = new_value
        else:
            self.value = 0

    def tick(self):
        """
        value를 1 증가시킨다.
        카운터의 값 value가 limit에 도달하면 value를 0으로 바꾼 뒤 True를 리턴한다.
        value가 limit보다 작은 경우 False를 리턴한다.
        """
        self.value += 1

        if self.value == self.limit:
            self.value = 0
            return True
        return False

    def __str__(self):
        """
        value를 최소 두 자릿수 이상의 문자열로 리턴한다.
        일단 str 함수로 숫자형 변수인 value를 문자열로 변환하고 zfill을 호출한다.
        """
        return str(self.value).zfill(2)


class Clock:
    """
    시계 클래스
    """

    HOURS = 24  # 시 최댓값
    MINUTES = 60  # 분 최댓값
    SECONDS = 60  # 초 최댓값

    def __init__(self, hour, minute, second):
        """
        각각 시, 분, 초를 나타내는 카운터 인스턴스 3개(hour, minute, second)를 정의한다.
        현재 시간을 파라미터 hour시, minute분, second초로 지정한다.
        """
        # Clock 안에서 Counter를 사용하는 생각
        self.hour = Counter(Clock.HOURS)
        self.minute = Counter(Clock.MINUTES)
        self.second = Counter(Clock.SECONDS)

        self.set(hour, minute, second)

    def set(self, hour, minute, second):
        """현재 시간을 파라미터 hour시, minute분, second초로 설정한다."""
        self.hour.set(hour)
        self.minute.set(minute)
        self.second.set(second)

    def tick(self):
        """
        초 카운터의 값을 1만큼 증가시킨다.
        초 카운터를 증가시킬 때, 분 또는 시가 바뀌어야하는 경우도 처리한다.
        """
        if self.second.tick():
            if self.minute.tick():
                self.hour.tick()

    def __str__(self):
        """
        현재 시간을 시:분:초 형식으로 리턴한다. 시, 분, 초는 두 자리 형식이다.
        예시: "03:11:02"
        """
        return "{}:{}:{}".format(self.hour, self.minute, self.second)


# 초가 60이 넘을 때 분이 늘어나는지 확인하기
print("시간을 1시 30분 48초로 설정합니다")
clock = Clock(1, 30, 48)
print(clock)

# 13초를 늘린다
print("13초가 흘렀습니다")
for i in range(13):
    clock.tick()
print(clock)

# 분이 60이 넘을 때 시간이 늘어나는지 확인
print("시간을 2시 59분 58초로 설정합니다")
clock.set(2, 59, 58)
print(clock)

# 5초를 늘린다
print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)

# 시간이 24가 넘을 때 00:00:00으로 넘어가는 지 확인
print("시간을 23시 59분 57초로 설정합니다")
clock.set(23, 59, 57)
print(clock)

# 5초를 늘린다
print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)

"""
* 코드 구동 방식 (이해가 안 되면 참고)
1. Clock 클래스의 인스턴스를 생성
2. 던더 init 에 hour 는 1, minute는 30, second는 48이 파라미터로 들어감
3. Counter 클래스의 인스턴스를 생성
4. Counter 클래스의 던더 init에 limit로 clock.HOURS(=24)가 들어감
5. Counter 클래스의 던더 init의 self.limit = limit 에 의해 인스턴스 변수인 limit 에 24가 할당
6. Counter 클래스의 던더 init의 self.value = 0 에 의해 인스턴스 변수인 value에 0이 할당
7. 다시 Clock 클래스의 던더 init으로 돌아가서 위에서 생성된 Counter 클래스의 인스턴스가 할당
8. 그러니 Counter 클래스의 인스턴스변수(limit, value) 와 메소드도 할당
9. 이런식으로 Clock 클래스의 던더 init의 인스턴스 변수인 hour, minute, second에 Counter 클래스의 인스턴스가 할당
10. 지금까지 Clock 클래스의 던더 init에 파라미터로 들어온 1, 30, 48 값은 쓰이지도 않음
11. Clock 클래스의 던더 init의 self.set(hour, minute, second)가 실행
12. 이제 여기서 1, 30, 48이 메소드의 인자로 들어감 (self.set(1, 30, 48)과 같음)
13. Clock 클래스의 set 메소드를 실행
14. self.hour.set(hour) 에서 set은 self.hour에는 Counter 클래스의 인스턴스가 할당되어 있으니 Couter 클래스의 set 메소드를 호출
15. hour가 1이니 self.hour에 할당된 Counter 클래스의 인스턴스변수인 value가 1
16. 이런식으로 self.hour.set(hour), self.minute.set(minute), self.second.set(second) 호출이 끝나면 Clock 클래스의 인스턴스 변수인 hour, mnute, second는 각각 value로(Counter 클래스의 인스턴스변수)로 1, 30, 48 을 가짐
17. 이렇게 던더 init 의 실행이 끝나고 생성된 인스턴스가 clock 변수에 할당
18. print(clock)을 하게 되면 Clock 클래스의 던더 str 이 호출
19. 던더 str 은 return "{}:{}:{}".format(self.hour, self.minute, self.second) 형태
20. 여기서 self.hour에는 Counter 클래스의 인스턴스가 할당되어 있으므로 Counter 클래스의 인스턴스를 가져오는 것이니, 이 역시 Counter 클래스의 던더 str을 호출
21. 결국 self.hour 는 Counter 클래스의 던더 str 을 호출하는 것
22. Counter 클래스의 던더 str 에는 return str(self.value).zfill(2) 이 포함
23. 이전에 9번째 순서에서 value로 1, 30, 48이 각 Clock 클래스의 인스턴스 변수인 hour, minute, second에 할당
24. 그래서 결국 print(clock)의 결과로 01:30:48이 출력
"""