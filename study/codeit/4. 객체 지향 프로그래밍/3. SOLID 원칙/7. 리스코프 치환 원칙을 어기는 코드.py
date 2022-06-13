class Employee:
    """직원 클래스"""

    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name = name
        self._wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self._wage *= self.raise_percentage

    @property
    def wage(self):
        return self._wage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class Cashier(Employee):
    """리스코프 치환 원칙을 지키지 않는 계산대 직원 클래스"""

    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def raise_pay(self, raise_amount):  # 부모 클래스에 없는 raise_amount를 추가하여 error가 생김
        """직원 시급을 인상하는 메소드"""
        self.wage += self.raise_amount

    @property
    def wage(self):  # 부모 클래스는 wage가 int이지만 자식 클래스에서 str로 바꾸어서 error가 생김
        return "시급 정보를 알려줄 수 없습니다"


employee_1 = Employee("성태호", 7000)
employee_2 = Employee("강영훈", 6500)

cashier = Cashier("김대위", 9000)

employee_list = []
employee_list.append(employee_1)
employee_list.append(employee_2)
employee_list.append(cashier)

for employee in employee_list:
    employee.raise_pay()  # 부모 클래스에 없는 raise_amount를 추가하여 error가 생김

total_wage = 0

for employee in employee_list:
    total_wage += employee.wage  # 부모 클래스는 wage가 int이지만 자식 클래스에서 str로 바꾸어서 error가 생김

print(total_wage)