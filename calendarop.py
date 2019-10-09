# PROVA CALENDARI
import datetime
from repo import MONTHS
#import calendar

day = "el 1 de octubre"
dl = day.split(' ')

msg = "dentista"


def validate(date_text):
    print("=======================")
    print(date_text)
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

# print (datetime.today().strftime('%Y-%m-%d'))

for i in dl:
    if i in MONTHS:
        m = str("{:02d}".format(MONTHS.index(i) + 1))
        print (m)
    elif i.isdigit():
        d = str("{:02d}".format(int(i)))
        print (d)
    #validate("2019" + '-' + m + '-' + d)
