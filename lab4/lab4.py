### 1

class Student:
    def __init__(self, name: str, marks: int):
        self.name=name
        self.marks=marks
        self.is_passed=marks > 50

    def __str__(self):
        return f'''
            Wynik egzaminu {self.marks} % {self.is_passed}
             '''

### 2

#a
class Library:
    def __init__(self, city: str, street: str,
                 zip_code: str, open_hours: str,phone: int):
        self.city=city
        self.street=street
        self.zip_code=zip_code
        self.open_hours=open_hours
        self.phone=phone



    def __str__(self):
        return f'''
            Lokalizacja: {self.city},
            Ulica: {self.street}, {self.zip_code},
            Otwarta w godz: {self.open_hours},
            Kontakt telefoniczny:  {self.phone} '''



#b
class Order:
    def __init__(self,employee: str, student: str, books: list, order_date: str):
        self.employee=employee
        self.student=student
        self.books=books
        self.order_date=order_date
        self.list_to_srt= ' '.join([str(elem) for elem in books])

    def __str__(self):
        return f'''
            ===============================================
            ===============================================
            DATA:
            {self.order_date}
            {self.employee}
            OSOBA WYPOŻYCZAJĄCA:
            {self.student}

            ZAWARTOŚĆ ZAMÓWIENIA:
            {self.list_to_srt}
            ===============================================
            ===============================================
                '''

#c
class Employye:
    def __init__(self, first_name: str,last_name: str,hire_date: str,birth_date: str,city: str,street: str,zip_code: str,phone: int):
        self.first_name=first_name
        self.last_name=last_name
        self.hire_date=hire_date
        self.birth_date=birth_date
        self.city=city
        self.street=street
        self.zip_code=zip_code
        self.phone=phone

    def __str__(self):
        return f'''
            PRACOWNIK: 
            {self.first_name} {self.last_name}
            zatrudniony {self.hire_date}
            urodzony {self.birth_date}
            {self.city}
            ul. {self.street}, {self.zip_code}
            kontakt {self.phone}
            '''


#d
class Book:
    def __init__(self,library,name: str, publication_date: str, author_name: str, author_surname: str, number_of_pages: int):
        self.libary=library
        self.name=name
        self.publication_date=publication_date
        self.author_name=author_name
        self.author_surname=author_surname
        self.number_of_pages=number_of_pages

    def __str__(self):
        return f'''
            {self.libary},
            Tytuł: {self.name},
            publikacja:  {self.publication_date},
            autor: {self.author_name} {self.author_surname},
            liczba stron {self.number_of_pages}
                '''



# 2 biblioteki 
library1= Library('Dąbrowa Górnicza', 'Mickiewicza 5', "41-300", '7.00-15.00', 666666666 )
library2= Library('Katowice', 'Norwida12', "41-400", '8.00-13.00', 777777777 )

# 5 książki 
book1=Book(library1,'book1',1999,'Autor1_name','Autor1_surname',928)
book2=Book(library1,'book2',1989,'Autor2_name','Autor2_surname',123)
book3=Book(library1,'book3',2012,'Autor3_name','Autor3_surname',435)
book4=Book(library2,'book4',1990,'Autor4_name','Autor4_surname',223)
book5=Book(library2,'book5',2014,'Autor5_name','Autor5_surname',420)

# 3 pracownicy
pracownik1=Employye('Jan', 'Kowalski', '25.07.2021', '06.09.1990', 'Katowice','Uliczna 12','11-111',123321123)
pracownik2=Employye('Norber','Budny','22.08.2005','07.10.1995','Katowice','Przydrożna 21','22-222',321321321)
pracownik3=Employye('Jakub', 'Przegrałek','21.03.2001','24.04.1995','Dąbrowa Górnicza','Kopernika 32', '33-333',999998997)


# 2 zamowienia
zamowienie1 =Order(pracownik1,'student1',[book1,book2,book3],'14.02.2021')
zamowienie2=Order(pracownik3,'student2',[book4,book5],'18.03.2021')



### zad 3
class Property:
    def __init__(self, area: int,rooms: int,price:int ,address: str):
        self.area=area
        self.rooms=rooms
        self.price=price
        self.address=address

        
class House(Property):
    def __init__(self, area: int, rooms: int, price: int, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot=plot
    def __str__(self) -> str:
        return f'''
            #####################################
            Obszar: {self.area} m^2,
            Liczba pokoi: {self.rooms},
            Cena: {self.price} $$$,
            Adres: {self.address},
            płot: {self.plot} m
            #####################################
        '''

class Flat(Property):
    def __init__(self, area: int, rooms: int, price: int, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor=floor

    def __str__(self) -> str:
        return f'''
            #####################################
            Obszar: {self.area} m^2,
            Liczba pokoi: {self.rooms},
            Cena: {self.price} $$$,
            Adres: {self.address},
            podłoga {self.floor} m2
            #####################################
        '''


    



if __name__ == '__main__':
    print('zad1')
    print(Student('Maciek',49))
    print('zad2')
    print(zamowienie1)
    print(zamowienie2)
    print('zad3')
    print(House(59,3,300000,'Uliczna12',80))
    print(Flat(74,4,500000,'Uliczna12123',123))