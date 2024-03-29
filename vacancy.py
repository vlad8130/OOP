class UnableToWorkException(Exception):
    pass


class Candidate:
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def work(self):
        if self.work:
            raise UnableToWorkException("I’m not hired yet, lol.")

    @classmethod
    def from_csv(cls, string):
        try:
            first_name, last_name = string.split(' ', 1)
        except ValueError:
            first_name = string
            last_name = ''

        return cls(first_name, last_name)


class Vacancy:
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level
