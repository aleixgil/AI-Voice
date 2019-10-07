from ttos import Ttos
from repo import MONTHS, ALARM_F
import datetime

class Timeop:

    def currentTime(self):
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        Ttos().say("Són las {} y {}.".format(hour, minute))
        print("Són las {} y {}.".format(hour,minute))

    def currentDate(self):
        year = datetime.datetime.now().year
        day = datetime.datetime.now().day
        month = MONTHS[datetime.datetime.now().month - 1]
        Ttos().say("Hoy es {} de {} de {}.".format(day, month, year))

    def alarm(self, text):
        # Lima, pon/ponme/poner alarma a las X
        # ... mañana a las X
        # ... mañana a las X de la mañana/mediodia/tarde/noche
        # ... pasado mañana a las X ...
        # ... el dia X a las X
        # ... en X h/min/sec
        # ... para dormir X h
        # COMPROVAR QUE TRADUEIX SI DIC LES 12:30
        pass
        
    def set_alarm(self, year, month, day, hour, minute):
        #hour = datetime.datetime.now().hour
        #minute = datetime.datetime.now().minute
        #day = datetime.datetime.now().day
        #month = datetime.datetime.now().month
        #year = datetime.datetime.now().year
        ALARM_F[1] = "{}/{}/{} {}:{}".format(year, month, day, hour, minute)
        ALARM_F[0] = True

    def check_alarm(self):
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        day = datetime.datetime.now().day
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        date_alarm = "{}/{}/{} {}:{}".format(year, month, day, hour, minute)
        return (date_alarm == ALARM_F[1])

    def validate_day(self, d):
        try:
            datetime.datetime.strptime(d, "%Y/%m/%d") # year/month/day
        except:
            print("WRONG DAY")

    def validate_hour(self, h):
        try:
            datetime.datetime.strptime(h, "%H:%M") # hour:minute
        except:
            print("WRONG HOUR")

    def validate_date(self, d):
        try:
            datetime.datetime.strptime(d, "% Y/%m/%d %H:%M")
        except:
            print("WRONG DATE")
