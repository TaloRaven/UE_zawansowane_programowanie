
class Kurs:
    def __init__(self, pojazd, odcinki, firmaspozywcza, firma_transportowa):
        self.pojazd = pojazd
        self.odcinki=odcinki
        self.firmaspozywcza=firmaspozywcza
        self.firma_transportowa=firma_transportowa
        self.kilomtery=2
        #self.suma=sum(self.odcinki)
        n=0




    def suma(self):
        n=0
        for i in self.odcinki:
            n+=i,2
        return round(n, 2)
    @property
    def marka(self):
        return Pojazd().marka


    def __str__(self):
        return f'''kurs zrobiony prez pojazd {self.pojazd}
            FIRMA TRANSPORETOWA 
                {self.firma_transportowa},
            POJAZD
                {self.pojazd}
            OCINKI  
                {self.odcinki}
            FRIMA SPOŻYWCZA  
                {self.firmaspozywcza}
            SUMA
                '''


class Pojazd:
        def __init__(self, marka: str,pojemnosc: int, przebieg: int, naped: str, rocznik: int):
            self.przebieg = przebieg
            self.marka=marka
            self.pojemnosc=pojemnosc
            self.naped=naped
            self.rocznik=rocznik

        def __str__(self):
            return f''' samochód marki {self.marka}, o pojemnosci {self.pojemnosc} o przebiegu {self.przebieg} z napędem na {self.naped} wyprodukowany w roku {self.rocznik} '''

class Firma:
    def __init__(self, nazwa: str, ulica: str, wlasciciel: str):
        self.nazwa=nazwa
        self.ulica=ulica
        self.wlascicel=wlasciciel
        

class FirmaTransportowa(Firma):
    def __init__(self, liczba_pojazdow: int, pojazdy: str, nazwa: str, ulica: str, wlasciciel: str):
        super().__init__(nazwa, ulica, wlasciciel)
        self.liczba_pojazdow=liczba_pojazdow
        self.pojazdy=pojazdy
        
    def __str__(self)->str:
        return f'Firma transportowa {self.nazwa} umiejscowoiona na ulicy {self.ulica} zarzadzana przez {self.wlascicel}.' \
               f'liczba pojazdow na stanie {self.liczba_pojazdow}, pojazdy te to {self.pojazdy}'


class FirmaSpozywcza(Firma):
    def __init__(self, nazwa: str, ulica: str, wlasciciel: str, zamowienie: str, wartosc_zam: int):
        super().__init__(nazwa, ulica, wlasciciel)
        self.wartosc_zam = wartosc_zam
        self.zamowienie = zamowienie

    def __str__(self):
        return f'Firma transportowa {self.nazwa} umiejscowoiona na ulicy {self.ulica} zarzadzana przez {self.wlascicel}.' \
               f'Wartosc zamowienia  {self.wartosc_zam}, zamowienie {self.zamowienie}'
        


class Odcinek:
    def __init__(self, start: str, finish: str, odleglosc: float, odbiorca: str,kierowca: str ):
        self.start=start
        self.finish=finish
        self.odleglosc=odleglosc
        self.odbiorca=odbiorca
        self.kierowca=kierowca

    
    def __str__(self)->str:
        return f'''Odcinek od {self.start} do {self.finish} o odleglosci {self.odleglosc} do {self.odbiorca} pojazd prowadzony prezez {self.kierowca}
                        '''


pojazd1=Pojazd('Skoda',300,400000,'4 kola',2008)

odcinek1=Odcinek('Dąbrowa',"katowcie",15.678,'janek','darek')
odcinek2=Odcinek("katowcie",'Dąbrowa',15.678,'kuba','piotrek')
odcink1=[odcinek1,odcinek2]

firmaspozywcza1=FirmaSpozywcza('podwarzywniakiem','uliczna','piotrek','2351',289)
firmatransportowa1=FirmaTransportowa(2,str([pojazd1]),'Transport na kozku','2terminy 12','Wojtek')

kurs_1=Kurs(pojazd1 ,odcink1,firmaspozywcza1,firmatransportowa1)


if __name__ == '__main__':
    print(kurs_1)