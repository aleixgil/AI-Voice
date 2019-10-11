from ttos import Ttos
from repo import MONTHS, ALARM_F
import datetime

class Timeop:
    '''
    Classe amb respostes relacionades amb el temps.
    '''
    
    def currentTime(self):
        '''
        Retorna la hora actual.
        '''
        hms = str(datetime.datetime.today()).split(' ')[1].split(':')  # Llista amb la hora, els minuts i els segons actuals
        return(Ttos().say("Són las {} y {}.".format(hms[0], hms[1])))

    def currentDate(self):
        '''
        Retorna la data actual.
        '''
        ydmtd = str(datetime.datetime.today()).split(' ')[0].split('-')  # Llista amb l'any, el mes i el dia d'avuí
        return(Ttos().say("Hoy es {} de {} de {}.".format(ydmtd[2], MONTHS[int(ydmtd[1]) - 1], ydmtd[0])))

    def tomorrowDate(self):
        '''
        Retorna la data de demà
        '''
        ydmtw = str(datetime.datetime.today() + datetime.timedelta(days=1)).split(' ')[0].split('-')  # Llista amb l'any, el mes i el dia de demà
        return(Ttos().say("Mañana será {} de {} de {}.".format(ydmtw[2], MONTHS[int(ydmtw[1]) - 1], ydmtw[0])))

    def alarm(self, text):
        '''
        Funció gestió de l'alarma.
        '''
        h, m = "", "00"
        d = str(datetime.datetime.today()).split(' ')[0]
        dm = str(datetime.datetime.today() + datetime.timedelta(days=1)).split(' ')[0]

        for wd in text.split(' '): # h
            if wd.isdigit():
                h = wd
            elif ":" in wd: # h:m
                h, m = wd.split(':')[0], wd.split(':')[1]

        # Diferents maneres de ordenar posar l'alarma
        if ("mañana" in text):
            self.set_alarm(dm, h, m)
        else:
            if datetime.datetime.now().hour < 12:
                if (int(h) < 12) and (self.validate_hour(h, m) == False):
                    self.set_alarm(d, str(int(h)+12), m)
                else:
                    self.set_alarm(d, h, m)
            else:
                if int(h) < 12:
                    if self.validate_hour(str(int(h)+12), m):
                        self.set_alarm(d, str(int(h)+12), m)
                    else:    
                        self.set_alarm(dm, h, m)
                else:
                    if self.validate_hour(h, m):
                        self.set_alarm(d, h, m)
                    else:
                        self.set_alarm(dm, str(int(h)-12), m)
        
    def set_alarm(self, ymd, hour, minute):
        '''
        Activar alarma.
        '''
        ALARM_F[1] = "{} {}:{}".format(ymd, hour, minute)
        Ttos().say("Alarma programada para las {} {}.".format(hour, minute))

    def check_alarm(self):
        '''
        Comprovar l'hora de l'alarma.
        '''
        t = datetime.datetime.now()
        date_alarm = "{}-{}-{} {}:{}".format(t.year, t.month, t.day, t.hour, t.minute)
        return (date_alarm == ALARM_F[1])

    def validate_hour(self, h, m):
        '''
        Comprovació de l'hora actual.
        '''
        if h.isdigit():
            if (int(h) > datetime.datetime.today().hour) or ((int(h) == datetime.datetime.today().hour) and (int(m) > datetime.datetime.today().minute)):
                return(True)
        return(False)

