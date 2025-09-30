f = open("Dane/liczby_przyklad.txt")
lista = []
for i in f:
    lista.append(i)
pierwsza = lista[0].rstrip().split(" ")
druga = lista[1].split(" ")
print(pierwsza)
print(druga)

pierwsza = [int(i) for i in pierwsza]
druga = [int(i) for i in druga]

c = 0
p = []
for y in pierwsza:
    for x in druga:
        if x % y ==0:
            break
print(c)
pierwsza.sort()
print(pierwsza[100])

slownik = dict.fromkeys(pierwsza, 0)
for i in pierwsza:
    slownik[i]+=1
print(slownik)
lista_czynnikow = list(slownik.keys())
print(lista_czynnikow)

print(pierwsza.count(3))

def naDzielniki(liczba:int):
    dzielniki = []
    dzielnik = 2
    while liczba > 1:
        if liczba % dzielnik == 0:
            dzielniki.append(dzielnik)
            liczba = liczba // dzielnik
        else:
            dzielnik+=1
    return dzielniki
odpowiedz = []
for i in druga:
    flaga = False
    rozbite = naDzielniki(i)
    rozbite_pojedyncze = list(dict.fromkeys(rozbite))
    for dzielnik in rozbite_pojedyncze:
        if rozbite.count(dzielnik) > pierwsza.count(dzielnik):
            print("nie")
            flaga = True
            break
    if not flaga:
        odpowiedz.append(i)

print(list(dict.fromkeys(odpowiedz)))