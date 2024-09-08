import datetime
from dateutil.relativedelta import relativedelta


def print_custom_message(name, year, month, day):
    result = relativedelta(datetime.date.today(), datetime.date(year, month, day)).years
    months = relativedelta(
        datetime.date.today(), datetime.date(year, month, day)
    ).months
    return f"Hello {name}, you are {result} years old and {months} months"


if __name__ == "__main__":
    print(print_custom_message("Alejandro", 2000, 2, 5))
