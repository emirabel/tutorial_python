# -*- coding: utf-8 -*-#
import datetime
def print_header():
    print('-----------------------------------')
    print('        Cumpleaños')
    print('-----------------------------------')
    print('')

def get_birthday_from_user():
    print('Dime tu fecha de nacimiento: ')
    year = int(input('Año [YYYY]: '))
    month = int(input('Mes [MM]: '))
    day = int(input('Dia [DD]: '))
    birthday = datetime.date(year, month, day)
    return birthday

def compute_days_between_dates(original_date, now):
    date1 = now
    date2 = datetime.date(now.year, original_date.month, original_date.day)
    dt = date1 - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days

def print_birthday_information(days):
    if days < 0:
        print('Tu cumple es en {} dias!'.format(-days))
    elif days > 0:
        print('Tuviste tu cumpleaños hace {} días'.format(days))
    else:
        print('Feliz cumlpeaños!!!')

def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)
main()