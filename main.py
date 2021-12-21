from Models.Zamowienie import Zamowienie
from Models.Developer import Developer
from Models.NIeruchomosc import Mieszkanie, Dom


developer1 = Developer('Maciej', 'Gardzinski', 'maciek@gmaill.com', 123123123)
m1 = Mieszkanie(50, "dg", developer1, 2, 300000, 3, True, True)
d1 = Dom(60, 'dg', developer1, 5, 500000, True, False, 2)
zam1 = Zamowienie()

zam1.developer(developer1)
zam1.data('13.13.13')
zam1.odbiorca('marek')
zam1.nieruchomosci([m1, d1])


if __name__ == '__main__':
    print(zam1)
