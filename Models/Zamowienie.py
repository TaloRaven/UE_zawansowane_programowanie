from Models.NIeruchomosc import Nieruchomosc
from Models.utils import wartosc_zamowienia, laczny_metraz


class Zamowienie:

    def __init__(self, developer, nieruchomosci: list, data, odbiorca):
        self.developer = developer
        self.nieruchomosci = nieruchomosci
        self.list_to_srt = ' '.join([str(elem) for elem in nieruchomosci])
        self.data = data
        self.odbiorca = odbiorca
        self.sum_zam = wartosc_zamowienia(nieruchomosci)
        self.sum_metraz = laczny_metraz(nieruchomosci)

    @property
    def developer(self):
        return self._developer

    @developer.setter
    def developer(self, developer):
        self.developer = developer

    @property
    def nieruchomosci(self):
        return self._nieruchomosci

    @nieruchomosci.setter
    def developer(self, nieruchomosci: list):
        self.nieruchomosci = nieruchomosci

    @property
    def data(self):
        return self._data

    @data.setter
    def developer(self, data: str):
        self.data = data

    @property
    def odbiorca(self):
        return self._odbiorca

    @odbiorca.setter
    def odbiorca(self, odbiorca):
        self.odbiorca = odbiorca

    def __str__(self) -> str:
        return f'''{self.developer}
                   Nieruchomosci: {self.list_to_srt}
                   data: {self.data}
                   odbiorca: {self.odbiorca}
                   wartosc zamowienia: {self.sum_zam}
                   laczny_metraz: {self.sum_metraz}
                  '''
