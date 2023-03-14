import random
import datetime


def rand_date(str_date1, str_date2):
    """
    The function get two strings of time in the format <%Y-%m-%d>
    and returns a random date between them.
    :param str_date1: first date
    :param str_date2: second date
    :return: random date between (str_date1, str_date2)
    """
    date1 = datetime.datetime.strptime(str_date1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(str_date2, '%Y-%m-%d')
    if date1.time() <= date2.time():
        return date1 + (date2 - date1) * random.random()
    else:
        return None


def main():
    str_date1 = input('Enter first date:\n')
    str_date2 = input('Enter second date:\n')
    try:
        new_date = rand_date(str_date1, str_date2)
        if new_date and new_date.weekday() == 0:
            print('I have no vinigret!')
            print(f'{new_date.strftime("%Y-%m-%d")}\nfinish')
        else:
            print('Oops! Make sure that the first date is earlier than the second and try again')
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
