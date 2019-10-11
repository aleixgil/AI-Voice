import datetime
from repo import CN,MONTHS
from ttos import Ttos

class Calendarop:
    '''
    Classe amb respostes relacionades amb el recordatori d'informació
    '''

    def takeNote(self, text):
        '''
        Funció per apuntar una recordatori.
        '''
        n = ""
        y = str(datetime.datetime.now().year)
        m = str(datetime.datetime.now().month)
        d = str(datetime.datetime.now().day)

        for wd in text.split(' '):  # h
            if wd.isdigit():
                d = wd
            elif wd in MONTHS:
                m = str(MONTHS.index(wd)+1)
        n = text.split("apuntar", 1)[1]
        if "mañana" in text:
            n = text.split("mañana", 1)[1]
            d = str(datetime.datetime.today() + datetime.timedelta(days=1)).split(' ')[0].split('-')[2]
        elif d in text:
            n = text.split(MONTHS[int(m)-1], 1)[1]
        else:
            n = text.split("apuntar", 1)[1]

        if n != "":
            CN.append(("{}-{}-{}".format(y,m,d),n))
            Ttos().say("Apuntado para el dia {} de {}: {}".format(d,MONTHS[int(m) - 1],n))
        else:
            Ttos().say("Lo siento, no te he entendido.")

    def goodm(self):
        '''
        Funció per saber els recordatoris del dia
        '''
        Ttos().say("Buenos días")
        if CN != []:
            currentdate = str(datetime.datetime.today()).split(' ')[0]
            f = 0
            for n in CN:
                if n[0] == currentdate:
                    if f == 0:
                        Ttos().say("hoy tienes")
                        f = 1
                    Ttos().say(n[1])
        else:
            Ttos().say("hoy no tienes nada pendiente")
