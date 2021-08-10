def validate_email():
    with open("emails.txt", "a+") as f:
        for line in f:
            if line in f.read():
                raise ValueError("Email you're entering already exists!")
            # try:
            #     self.email == self.email
            # except ValueError:
            #     print("")


class Employee:

    def __init__(self, name, salary, working_days, email):
        self.name = name
        self.salary = salary
        self.working_days = working_days
        self.email = email
        self.save_email()
        validate_email()

    def save_email(self):
        with open("emails.txt", "a+") as f:
            f.write(self.email)

    def work(self):
        return "I come to the office."

    def check_salary(self):
        salary = self.salary
        working_days = self.working_days
        return salary * working_days

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class Programmer(Employee):

    def __init__(self, name, salary, working_days, email, tech_stack):
        self.tech_stack = tech_stack
        super().__init__(name, salary, working_days, email)

    def work(self):
        emp_work = super().work()[:-1]
        emp_check_salary = super().check_salary()
        return print(emp_work + " and start coding.", 'I have earned :', emp_check_salary, '$')

    def __str__(self):
        name = self.name
        return (print("Programmer:", name))


class Programmer2(Employee):
    tech_stack = ['JavaScript', 'Python', 'C++', 'PHP', 'SQL', 'Java']

    def __init__(self, name, salary, working_days, email, tech_stack):
        self.tech_stack = tech_stack
        super().__init__(name, salary, working_days, email)

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
