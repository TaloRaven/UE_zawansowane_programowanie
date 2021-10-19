

## Zad2

#a
names=['Maciej','Kamil','Kuba','norbert','Jarek']
def imiona(names):
    return names

#b

#b_I
liczby=[5,8,9,12,3]

def mozenie(liczby):
    n_liczby=[]
    for x in liczby:
        n_liczby.append(x*2)
    return n_liczby

#b_II
liczby_2=[5,8,9,12,3]
mnozenie_2 = [liczba*2 for liczba in liczby_2]


#c
liczby_1=[1,2,3,4,5,6,7,8,9,10]

def parzyste(liczby_1):
    liczby_p=[]
    for x in range(len(liczby_1)-1):
        if x ==0:
            continue
        elif x % 2==0:
            liczby_p.append(x)
        else:
            continue
    return liczby_p

#d
liczby_2=[5,10,8,29,18,28,24,15,23,17]

def co_druga(liczby_2):
    liczby_p=[]
    for x in range(len(liczby_2)):
        if x % 2!=0:
            liczby_p.append(liczby_2[x])
        else:
            continue
    return liczby_p


if __name__ == '__main__':
    print(imiona(names))
    print(mozenie(liczby))
    print(mnozenie_2)
    print(parzyste(liczby_1))
    print(co_druga(liczby_2))




