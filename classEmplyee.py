class Employee:
    def __init__(self, first_name, last_name, social):
        self._first_name = first_name
        self._last_name = last_name
        self._social = social

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def social(self):
        return self._social

    def earnings(self):
        pass

    def __repr__(self):
        return f"Name: {self._first_name} {self._last_name}, Social: {self._social}"


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, social, weekly_salary):
        Employee.__init__(self, first_name, last_name, social)
        self._weekly_salary = max(0, weekly_salary)

    @property
    def weekly_salary(self):
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, value):
        if value < 0:
            self._weekly_salary = 0
        else:
            self._weekly_salary = value

    def earnings(self):
        return self._weekly_salary

    def __repr__(self):
        return f"Salaried Employee: {Employee.__repr__(self)}"


class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, social, hours, wage_per_hour):
        Employee.__init__(self, first_name, last_name, social)
        self._hours = max(0, hours)
        self._wage_per_hour = max(0, wage_per_hour)

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        self._hours = max(0, value)

    @property
    def wage_per_hour(self):
        return self._wage_per_hour

    @wage_per_hour.setter
    def wage_per_hour(self, value):
        self._wage_per_hour = max(0, value)

    def earnings(self):
        if self._hours <= 40:
            return self._hours * self._wage_per_hour
        else:
            regular_pay = 40 * self._wage_per_hour
            overtime_pay = (self._hours - 40) * (1.5 * self._wage_per_hour)
            return regular_pay + overtime_pay

    def __repr__(self):
        return f"Hourly Employee: {Employee.__repr__(self)}"


def main():
    salaried_emp = SalariedEmployee("Alice", "Smith", "987-65-4321", 1000)
    hourly_emp = HourlyEmployee("Bob", "Johnson", "456-78-9123", 45, 20)

    print(salaried_emp)
    print("Earnings:", salaried_emp.earnings())

    print(hourly_emp)
    print("Earnings:", hourly_emp.earnings())


main()
