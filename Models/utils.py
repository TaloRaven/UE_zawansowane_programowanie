from Models.Zamowienie import Zamowienie
from Models.Developer import Developer
from Models.NIeruchomosc import Mieszkanie, Dom


def wartosc_zamowienia(self,nieruchomosc):
    n=0
    for i in nieruchomosc:
        n+=nieruchomosc.cena
    return n

def laczny_metraz(self, nieruchomosc):
    n=0
    for i in nieruchomosc:
        n += nieruchomosc.metraz
    return n


