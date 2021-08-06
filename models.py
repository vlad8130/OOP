class Employee:

    def __init__(self, name, salary, working_days):
        self.name = name
        self.salary = salary
        self.working_days = working_days

    def work(self):
        return "I come to the office."

    def check_salary(self):
        salary = self.salary
        working_days = self.working_days
        return salary * working_days


class Programmer(Employee):
    tech_stack = ['JavaScript', 'Python', 'C++', 'PHP', 'SQL', 'Java']

    def __init__(self, name, salary, working_days, tech_stack):
        tech_stack = self.tech_stack
        super().__init__(name, salary, working_days)

    def work(self):
        emp_work = super().work()[:-1]
        emp_check_salary = super().check_salary()
        return (print(emp_work + " and start coding.", 'I have earned :', emp_check_salary, '$'))

    def __str__(self):
        name = self.name
        return (print("Programmer:", name))


class Programmer2(Employee):
    tech_stack = ['JavaScript', 'Python', 'C++', 'PHP', 'SQL', 'Java']

    def __init__(self, name, salary, working_days, tech_stack):
        tech_stack = self.tech_stack
        super().__init__(name, salary, working_days)

    def work(self):
        emp_work = super().work()[:-1]
        emp_check_salary = super().check_salary()
        return (print(emp_work + " and start coding.", 'I have earned :', emp_check_salary, '$'))

    def __str__(self):
        name = self.name
        return (print("Programmer_2 :", name))


class Recruiter(Employee):
    def work(self):
        emp_work = super().work()[:-1]
        emp_check_salary = super().check_salary()
        return (print(emp_work + " and start hiring.", 'I have earned :', emp_check_salary, '$'))

    def __str__(self):
        name = self.name
        return (print("Recruiter :", name))
