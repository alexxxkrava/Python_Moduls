from datetime import datetime
from Applications.Salary import calculate_salary
from Applications.db.people import get_employees
import emoji

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(f'Did you see what time it is??')
    print(datetime.now())
    print(emoji.emojize(':frowning_face:'))