

class Nieruchomosc:
    def __init__(self, metraz: int, lokalizacja: str,
                 wlasciciel: str, liczba_pokoi: str, cena: int):
        self.metraz = metraz
        self.lokalizacja = lokalizacja
        self.wlasciciel = wlasciciel
        self.liczba_pokoi = liczba_pokoi


class Dom(Nieruchomosc):
    def __init__(
            self,
            metraz: int,
            lokalizacja: str,
            wlasciciel: str,
            liczba_pokoi: str,
            cena: int,
            ogrodek: bool,
            garaz: bool,
            liczba_pieter: int):
        super().__init__(metraz, lokalizacja, wlasciciel, liczba_pokoi, cena)
        self.ogrodek = ogrodek
        self.garaz = garaz
        self.liczba_pieter = liczba_pieter

    def __str__(self) -> str:
        return f'''Dom o metrazu {self.metraz},
         na ulicy {self.lokalizacja}, wlasnosc {self.wlasciciel}, z liczba pokoi {self.liczba_pokoi} .
         Ogordek:{self.ogrodek}
         garaz:{self.garaz}
         liczba_pieter:{self.liczba_pieter}'''


class Mieszkanie(Nieruchomosc):
    def __init__(
            self,
            metraz: int,
            lokalizacja: str,
            wlasciciel: str,
            liczba_pokoi: str,
            cena: int,
            pietro: int,
            balkon: bool,
            winda: bool):

        super().__init__(metraz, lokalizacja,
                         wlasciciel, liczba_pokoi, cena)
        self.piertro = pietro
        self.balkon = balkon
        self.winda = winda

    def __str__(self) -> str:
        return f'''Mieszkanie o metrazu {self.metraz},
         na ulicy {self.lokalizacja}, wlasnosc {self.wlasciciel}, z liczba pokoi {self.liczba_pokoi}
         pietro:{self.piertro}
         balkon:{self.balkon}
         winda:{self.winda}'''
