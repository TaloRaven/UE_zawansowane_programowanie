from Biblioteka.Book import Book
from Biblioteka.Order import Order
from Biblioteka.Student import Student
from Biblioteka.Library import  Library
from Biblioteka.Employye import  Employye

# 2 biblioteki
library1 = Library(
    'Dąbrowa Górnicza',
    'Mickiewicza 5',
    "41-300",
    '7.00-15.00',
    666666666)

library2 = Library('Katowice', 'Norwida12', "41-400", '8.00-13.00', 777777777)

# 5 książki
book1 = Book(library1, 'book1', 1999, 'Autor1_name', 'Autor1_surname', 928)
book2 = Book(library1, 'book2', 1989, 'Autor2_name', 'Autor2_surname', 123)
book3 = Book(library1, 'book3', 2012, 'Autor3_name', 'Autor3_surname', 435)
book4 = Book(library2, 'book4', 1990, 'Autor4_name', 'Autor4_surname', 223)
book5 = Book(library2, 'book5', 2014, 'Autor5_name', 'Autor5_surname', 420)

# 3 pracownicy
pracownik1 = Employye(
    'Jan',
    'Kowalski',
    '25.07.2021',
    '06.09.1990',
    'Katowice',
    'Uliczna 12',
    '11-111',
    123321123)
pracownik2 = Employye(
    'Norber',
    'Budny',
    '22.08.2005',
    '07.10.1995',
    'Katowice',
    'Przydrożna 21',
    '22-222',
    321321321)
pracownik3 = Employye(
    'Jakub',
    'Przegrałek',
    '21.03.2001',
    '24.04.1995',
    'Dąbrowa Górnicza',
    'Kopernika 32',
    '33-333',
    999998997)

# 2 zamowienia
zamowienie1 = Order(
    pracownik1, 'student1', [
        book1, book2, book3], '14.02.2021')
zamowienie2 = Order(pracownik3, 'student2', [book4, book5], '18.03.2021')