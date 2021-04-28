#zadanie1
'''
lista = [1, 2, 3, 4, 5, 6]
def ostatni(lista):
    if len(lista) > 1:
        return ostatni(lista[1:])
    else:
        return lista

print(ostatni(lista))
'''
#zadanie2
#chyba dobrze(?)
'''
lista_nowa=[]
def ogon(lista):
    if len(lista) > 1:
        lista_nowa.append(lista[-1])
        return ogon(lista[:-1])
    else:
        lista_posortowana=[]
        for i in range(len(lista_nowa)-1,-1,-1):
            lista_posortowana.append(lista_nowa[i])
        return lista_posortowana

lista=[1, 2, 3, 4, 5]
print(ogon(lista))
'''
#zadanie3
'''
lista = [5, 4, 3, 6, 1]
def lista_najwiekszy(lista, maksimum):
    if len(lista)>0:
        if lista[0] > maksimum:
            maksimum=lista[0]
        return lista_najwiekszy(lista[1:], maksimum)
    else:
        return maksimum

print(lista_najwiekszy(lista,lista[0]))
'''
#zadanie4
'''
lista=[1,2,3,4,5,6]
def dlugosc(lista):
    if len(lista)>0:
        return 1+dlugosc(lista[1:])
    else:
        return 0
print(dlugosc(lista))
'''
#zadanie5
#nie rozumiem, skopiowałem
'''
lista = [1, 2, 3, 4, 5]
def nty(lista, element, licznik):
    if len(lista) > 0:
        if licznik == element:
            return lista[0]
        else:
            licznik+=1
            return nty(lista[1:], element, licznik)

print(nty(lista, 4, 1))
'''
#zadanie6
'''
def czy_element_jest_na_liscie(lista,element):
    if len(lista)>0:
        if element == lista[0]:
            return "tak"
        else:
            return czy_element_jest_na_liscie(lista[1:],element)
    else:
        return "nie"
lista=[1,2,3,4,5]
wynik=czy_element_jest_na_liscie(lista, 6)
print(wynik)
'''
#zadanie7
#nie umiem

#zadanie8
'''
def silnia(liczba):
    if liczba < 1:
        return 1
    else:
        return liczba * silnia (liczba - 1)

print(silnia(5))
'''
#zadanie9,10
'''
#wypisuje = print
def suma(x,y):
    return x+y

print(suma(5,3))
#zwraca = return (bez printa), idk coś w tym stylu
def suma(x,y):
    wynik=x+y
    return wynik

x=3
y=4
wynik_koncowy=suma(x,y)
print(wynik_koncowy)
'''
#zadanie11
'''
def odejmowanie(x,y):
    return x-y

def dodawanie(x,y):
    return x+y

print("Podaj pierwszą liczbę")
x=int(input())
print("Podaj drugą liczbę")
y=int(input())
print("Jakie działanie chcesz wykonać?")
odpowiedz=input()
wynik_dodawania=dodawanie(x,y)
wynik_odejmowania=odejmowanie(x,y)
if odpowiedz=="dodawanie":
    print(wynik_dodawania)
if odpowiedz=="odejmowanie":
    print(wynik_odejmowania)
'''
#zadanie12
'''
def rownosc(x,y):
    if x==y:
        return "są równe", 0
    else:
        return "nie są równe", ((x-y)**2)**(1/2)

print("Podaj pierwszą liczbę")
x=int(input())
print("Podaj drugą liczbę")
y=int(input())
równość, różnica=rownosc(x,y)
print(równość, "| różnica wynosi", różnica)
'''
#zadanie13
'''
def polaczenie(lista1,lista2):
    nowa_lista=lista1
    for i in range(len(lista2)):
        nowa_lista.append(lista2[i])
    return nowa_lista

lista1=[3,7,8]
lista2=[4,6,4,3,8]
polaczone_listy=polaczenie(lista1,lista2)
print(polaczone_listy)
'''
#zadanie14
'''
def polaczenie(lista1,lista2):
    nowa_lista=lista1
    for i in range(len(lista2)):
        if lista2[i] not in nowa_lista:
            nowa_lista.append(lista2[i])
    return nowa_lista

lista1=[3,7,8]
lista2=[4,6,4,3,8]
polaczone_listy=polaczenie(lista1,lista2)
print(polaczone_listy)
'''
#zadanie15
'''
def pierwiastek(liczba) :
    pierwiastek = liczba ** (0.5)
    pierwiastek = round(pierwiastek, 2)
    if pierwiastek%2 == 0 :
        return pierwiastek, "parzysta"
    else :
        return pierwiastek, "nieparzysta"



wynik, parzystosc = pierwiastek(8)
print(wynik, parzystosc)
'''
#zadanie16
'''
def dlugosc_maksimum(lista):
    maksymalna=lista[0]
    suma=0
    for i in lista:
        if i>maksymalna:
            maksymalna=i
        suma+=1
    return maksymalna, suma

lista=[1,2,-3,4,8,5,6,7,21]
maksymalny_element, dlugosc=dlugosc_maksimum(lista)
print("Największy element to:", maksymalny_element,", a długość to:", dlugosc)
'''

