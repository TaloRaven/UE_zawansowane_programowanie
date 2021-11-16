class Library:
    def __init__(self, city: str, street: str,
                 zip_code: str, open_hours: str, phone: int):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'''
            Lokalizacja: {self.city},
            Ulica: {self.street}, {self.zip_code},
            Otwarta w godz: {self.open_hours},
            Kontakt telefoniczny:  {self.phone} '''