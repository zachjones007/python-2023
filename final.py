import re


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


class CheckPass(Employee):
    def __init__(self, first_name, last_name, social, hours, wage_per_hour):
        Employee.__init__(self, first_name, last_name, social)
        Pass = str(input('Do you have a password?'))
        if Pass in ('Y', 'E', 'S'):
            with open('passwordlist.txt', 'r') as file:
                def extract_credentials(file_path):
                    with open(file_path, 'r') as file:
                        file_contents = file.read()

                    # Define a regular expression pattern to match username and password
                    pattern = r'Username: (\w+), Password: (\w+)'

                    # Find all matches in the file contents
                    matches = re.findall(pattern, file_contents)

                    # Extract usernames and passwords from matches
                    credentials = [(username, password) for username, password in matches]

                    # Example usage
                    file_path = 'passwordlist.txt'
                    credentials = extract_credentials(file_path)

                    # Print the extracted usernames and passwords
                    for username, password in credentials:
                        print(f'Username: {username}, Password: {password}')

                    EmployeeType = input('Are you a part-time or full-time employee? Enter 1 for part-time or 2 for full-time: ')
                    if EmployeeType == '1':
                        print("Earnings:", self.earnings())
                    else:
                        print("Earnings:", wage_per_hour.earnings())

                    return credentials
        else:
            while True:
                print('can you please create a password')
                def is_strong_password(password, name, birthdate):
                    if len(password) < 10:
                        print('Password must be at least 10 characters long.')
                        return False

                    if not re.search('[a-z]', password) or not re.search('[A-Z]', password):
                        print('Password must contain both lowercase and uppercase letters.')
                        return False

                    if not re.search('[0-9]', password):
                        print('Password must contain at least one digit.')
                        return False

                    if re.search(name, password, re.IGNORECASE):
                        print('Password must not contain your name.')
                        return False

                    if re.search(birthdate, password):
                        print('Password must not contain your birth year.')
                        return False

                    print('Password is strong.')
                    return True

                name = input('What is your username? ')
                birthdate = input('What is your birth year? ')
                password = input('Input a password: ')

                if is_strong_password(password, name, birthdate):
                    # Write password to file
                    with open('passwordlist.txt', 'a') as file:
                        file.write(password + '\n' + name + '\n')


def main():
    salaried_emp = SalariedEmployee("Alice", "Smith", "987-65-4321", 1000)
    hourly_emp = HourlyEmployee("Bob", "Johnson", "456-78-9123", 45, 20)
    check_pass = CheckPass("John", "Doe", "123-45-6789", 40, 25)


if __name__ == '__main__':
    main()
    print('Thank you')
