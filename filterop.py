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
        elif "día" in text:
            Timeop().currentDate()
        elif ("cero entre cero" or "cero dividido por cero") in text:
            Fun().cero()
        elif "alarma" in text:
            Timeop().alarm(text)
        else:
            Ttos().error()
            print("ERROR")
