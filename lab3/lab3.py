#1

def zad1(name: str, surname: str):
    text='Czesc {} {}!.'.format(name, surname)
    return text

#2
def zad2(liczba1: int,liczba2: int):
    return liczba1*liczba2

#3
def zad3(liczba: int):
    wynik=liczba%2==0
    if wynik is True :
        odp='liczba parzysta'
    else:
        odp='liczba nie parzysta'

    return odp
#4
def zad4(L1: int,L2: int,L3: int):
    wynik=L1+L2>=L3
    return wynik

#5
def zad5(lista: list, liczba: int):

	if liczba in lista:
		wynik="element w liscie"
	else:
		wynik="elemntu nie ma w liscie"
	return wynik

#6
def zad6(lista1: list, lista2: list):
    #zlaczyc
    lista3=lista1+lista2
    #bez duplikatow czyli jko set
    set1=set(lista3)
    lista3=list(set1)
    #kazdy leemnt do **3
    lista4=[]
    for x in lista3:
        lista4.append(x**3)
    #zwrocic liste
    return lista4

if __name__ == '__main__':
    print(zad1('Maciej', "Gardziński"))
    
    print(zad2(5,8))

    print(zad3(3))
    print(zad3(2))

    print(zad4(3,4,6))
    print(zad4(3,4,8))

    print(zad5([5,6,8,10],10))
    print(zad5([5,6,8,10],11))

    print(zad6([1,2,3],[4,5,6]))
    