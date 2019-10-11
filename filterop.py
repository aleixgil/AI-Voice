from calendarop import Calendarop
from timeop import Timeop
from ttos import Ttos
from fun import Fun

class Filterop:
    '''
    Classe per analitzar la frase de la pregunta i filtrar la resposta.
    '''
    def options(self, rec, mic, text):
        '''
        Funció d'anàlisis i filtratge.
        '''
        if "hora" in text:
            Timeop().currentTime()
        elif "buenos días" in text:
            Calendarop().goodm()
        elif ("día" in text) and ("mañana" in text):
            Timeop().tomorrowDate()
        elif "día" in text:
            Timeop().currentDate()
        elif "alarma" in text:
            Timeop().alarm(text)
        elif "apuntar" in text:
            Calendarop().takeNote(text)
        elif "edad" in text:
            Fun().age()
        elif ("cero entre cero" or "cero dividido por cero") in text:
            Fun().cero()
        else:
            Ttos().error()
