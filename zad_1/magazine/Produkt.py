import magazine.utils


class Produkt:

    def __init__(self,nazwa: str, marka: str, cena: int):
        self.nazwa=nazwa
        self.marka=marka
        self.cena=cena

    def __str__(self):
        return f'Nazwa: {self.nazwa}, marka: {self.marka}, cena: {self.cena}'


