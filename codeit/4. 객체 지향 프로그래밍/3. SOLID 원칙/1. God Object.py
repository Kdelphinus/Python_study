class Ship:
    """배 클래스"""

    def __init__(self, fuel, fuel_per_hour, supplies, num_crew):
        """연료량, 시간당 연료 소비량, 물자량, 선원 수를 인스턴스 변수로 갖는다"""
        self.fuel = fuel
        self.fuel_per_hour = fuel_per_hour
        self.supplies = supplies
        self.num_crew = num_crew

    def report_fuel(self):
        """연료량 보고 메소드"""
        print("현재 연료는 {}l 남아 있습니다".format(self.fuel))

    def load_fuel(self, amount):
        """연료 충전 메소드"""
        self.fuel += amount

    def report_supplies(self):
        """물자량 보고 메소드"""
        print("현재 물자는 {}명분이 남아 있습니다".format(self.supplies))

    def load_supplies(self, amount):
        """물자 보급 메소드"""
        self.supplies += amount

    def distribute_supplies_to_crew(self):
        """물자 배분 메소드"""
        if self.supplies >= self.num_crew:
            self.supplies -= self.num_crew
            return True
        print("물자가 부족하기 때문에 배분할 수 없습니다")
        return False

    def report_crew(self):
        """선원 수 보고 메소드"""
        print("현재 선원 {}명이 있습니다".format(self.num_crew))

    def load_crew(self, number):
        """선원 승선 메소드"""
        self.num_crew += number

    def run_engine_for_hours(self, hours):
        """엔진 작동 메소드"""
        if self.fuel > self.fuel_per_hour * hours:
            self.fuel -= self.fuel_per_hour * hours
            print("엔진을 {}시간 동안 돌립니다!".format(hours))
        else:
            print("연료가 부족하기 때문에 엔진 작동을 시작할 수 없습니다")


ship = Ship(400, 10, 1000, 50)

ship.load_fuel(10)

ship.load_supplies(10)

ship.load_crew(10)

ship.distribute_supplies_to_crew()

ship.run_engine_for_hours(4)

ship.report_fuel()
ship.report_supplies()
ship.report_crew()