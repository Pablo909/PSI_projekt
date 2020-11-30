def lista_laczona(a_list, b_list):
    c_list = []
    for index, wartosc in enumerate(a_list):
        if index % 2 == 0:
            c_list.append(wartosc)
    for index, wartosc in enumerate(b_list):
        if index % 2 == 1:
            c_list.append(wartosc)
    return c_list


def dane_tekstu(data_text):
    dane = {'length': len(data_text), 'letters': [char for char in data_text], 'big_letters': data_text.upper(),
            'small_letters': data_text.lower()}
    return dane


def usun_litery(text, letter):
    return text.replace(letter, '')


def przelicz_temperature(wartosc_celsjusz, temperature_type):
    if not wartosc_celsjusz.isdigit():
        return 'Wartość musi być liczbą.'
    else:
        wartosc_celsjusz = float(wartosc_celsjusz)
        if temperature_type == 'Fahrenheit':
            wartosc = 32 + 1.8 * wartosc_celsjusz
        elif temperature_type == 'Kelvin':
            wartosc = 273.15 + wartosc_celsjusz
        elif temperature_type == 'Rankine':
            wartosc = (273.15 + wartosc_celsjusz) * 1.8
        else:
            return 'Błędny typ temperatury(Fahrenheit, Kelvin, Rankine)'
        return wartosc


class Calculator:

    def add(self, a, b):
        return a+b

    def difference(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b


class ScienceCalculator(Calculator):
    def square(self, a):
        return a*a


def odwroc_string(tekscik):
    return tekscik[::-1]


# 1
lista_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_b = [-2, 5, 12, 34, 54, 12, 53]
print(lista_laczona(lista_a, lista_b))

# 2
tekst = 'Ola ma kota'
print(tekst)
print(dane_tekstu(tekst))

# 3
print(usun_litery(tekst, 'a'))

# 4
# celsjusz = input("Wprowadź temperaturę: ")
# typ_temperatury = input("Podaj typ temperatury: ")
# print(przelicz_temperature(celsjusz, typ_temperatury))

# 5
kalkulator = Calculator()
print(kalkulator.add(23, 67))
print(kalkulator.multiply(2, 23))

# 6
kalkulator_naukowy = ScienceCalculator()
print(kalkulator_naukowy.square(-2))

# 7
print(odwroc_string(tekst))
