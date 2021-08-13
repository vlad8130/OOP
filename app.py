import datetime
import traceback

from models import Employee
from models import Programmer
from models import Recruiter
from vacancy import Candidate, Vacancy


if __name__ == '__main__':
    prog = Programmer('Vladimir', 1500, 9, 'vlisitskiy@gmail.com', 'Python')
    prog2 = Programmer('John', 1000, 15, 'johnjohn@gmail.com', 'Java')
    recr = Recruiter('Petr', 500, 14, 'user@gmail.com')
    emp = Employee('Ivan', 450, 15, 'ivantsarevich@mail.com')
    cand = Candidate('Vasya', 'user1@mail.ru', 'computers', 'Computer Skills', 5)
    cand2 = Candidate('Anna', 'user2@mail.ru', 'Information Technology', 'Front End', 4)
    cand3 = Candidate('Epifaniy', 'user3@mail.ru', 'Software', 'Problem-Solving', 2)
    vac1 = Vacancy('Information Technology', 'Front End', 5)
    vac2 = Vacancy('Information Technology', 'Back End', 5)
    emp.work()
    prog.work()
    prog.__str__()
    recr.work()
    recr.__str__()
    # cand.work()


def logger_boy(func_to_wrap):
    def wrapper(*args, **kwargs):
        try:
            return func_to_wrap(*args, **kwargs)
        except Exception as err:
            with open('logs.txt', 'a') as f:
                message = '{}   {}:\n   {}\n\n'. format(datetime.datetime.now(),
                                                        err.__class__.__name__, traceback.format_exc())
                f.write(message)
    return wrapper()
