class Employee:

    def __init__(self, first_name, last_name, salary, working_days, email):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.working_days = working_days
        self.email = email
        self.validate_email()
        self.save_email()

    def validate_email(self):
        with open("emails.txt", "a+") as f:
            f.seek(0)
            if self.email in f.read():
                raise ValueError('Email is already taken.')

    def save_email(self):
        with open("emails.txt", "a+") as f:
            f.write(self.email + '\n')

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def work(self):
        return "I come to the office."

    def check_salary(self):
        salary = self.salary
        working_days = self.working_days
        return salary * working_days


class Programmer(Employee):

    def __init__(self, first_name, last_name, salary, working_days, email, tech_stack):
        self.tech_stack = tech_stack
        super().__init__(first_name, last_name, salary, working_days, email)

    def work(self):
        emp_work = super().work()[:-1]
        emp_check_salary = super().check_salary()
        return print(emp_work + " and start coding.", 'I have earned :', emp_check_salary, '$')

    # def __str__(self):
    #     self.name = name
    #     return (print("Programmer:", name))

# tech_stack = ['JavaScript', 'Python', 'C++', 'PHP', 'SQL', 'Java']


class Recruiter(Employee):
    def work(self):
        emp_work = super().work()[:-1]
        emp_check_salary = super().check_salary()
        return emp_work + " and start hiring.", 'I have earned :', emp_check_salary, '$'

    # def __str__(self):
    #     self.name = name
    #     return (print("Recruiter :", name))
