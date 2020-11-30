
# 1,2
a = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie = "Paweł"
nazwisko = "Bronk"
litera_1 = imie[2]
litera_2 = nazwisko[3]
print("W tekście jest %i liter %s oraz %i liter %s" % (a.count(litera_1), litera_1, a.count(litera_2), litera_2))

# 4
zmienna_typu_string = "Ciąg tekstowy"
print(dir(zmienna_typu_string))
# help(zmienna_typu_string.isupper())

# 5
print(imie[::-1].capitalize() + " " + nazwisko[::-1].capitalize())

# 6
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = list()
for i in range(5):
    lista2.append(lista.pop())
lista2.reverse()
print(lista)
print(lista2)

# 7
lista += lista2
lista.insert(0, 0)
lista3 = lista
print(sorted(lista3, reverse=True))

# 8
lista_studenci = [(150788, "Paweł Bronk"), (151100, "Mateusz Lewandowski"), (123412, "Bartek Glik"), (456313, "Kamil Milik")]
print(lista_studenci)

# 9
slownik_studenci = dict(lista_studenci)
print(slownik_studenci)

# 10
lista_telefon = [111222333, 222333444, 444333222, 111222333, 234567890, 444333222]
zbior_telefon = set(lista_telefon)
print(zbior_telefon)

# 11
for i in range(1, 11):
    print(i)

# 12
for i in range(100, 19, -5):
    print(i)

# 13
lista_slownikow = [{1: "jeden", 2: "dwa", 3: "trzy"}, {150788: ["Paweł", "Bronk"], 154123: ["Kamil", "Eeeee"]}]
for i in lista_slownikow:
    for j in i.keys():
        print("%s: %s" % (j, i[j]))
