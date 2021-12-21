
class Developer:
    def __init__(self, imie: str, nazwisko: str, mail: str, nr_tel: int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.mail = mail
        self.nr_tel = nr_tel

    def __str__(self) -> str:
        return f'''Developer {self.imie} {self.nazwisko}, kontakt email: {self.mail}, nr_tel: {self.nr_tel}  '''
