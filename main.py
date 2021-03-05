# Zad 1.
# Napisz skrypt, w którym tworzysz listę ulubionych sportów,
# odwróć ją a następnie dodaj mniej lubiane sporty na sam koniec.

# ulubione_sporty = ["piłka nożna", "palant", "bieg na krótki dystans"]
# ulubione_sporty.reverse()
# ulubione_sporty.append("skok w dal")
# ulubione_sporty.append("pchnięcie kulą")
# ulubione_sporty.append("siatkówka")
# print(ulubione_sporty)
########################################################################################################
# Zad 2.
# Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach internetowych.
# Jako klucz przyjmij skrót danego słowa, wartość to rozwinięcie tego skrótu.

# slownik = {'str': 'strona', 'tj': 'to jest', 'tzn': 'to znaczy' }
# print(slownik["tj"])
########################################################################################################
# Zad 3.
# Stwórz słownik z ulubionymi grami komputerowymi.
# Pomyśl, co może być kluczem a co wartością w takim słowniku. Policz liczbę elementów w słowniku.

# gry = {'LiS': 'Life is Strange', 'TES3': 'The Elder Scrolls III Morrowind', 'TWD': 'The Walking Dead', 'RDR2': 'Red Dead Redemption 2'}
# print(len(gry))
########################################################################################################
# Zad 4.
# Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a. Użyj funkcji input

# zdanie = input("Wpisz dowolne zdanie: ")
# substring = "a"
# count = zdanie.count(substring)
# print("Litera 'a' występuje ", count, "razy")
########################################################################################################
# Zad 5. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: a^b + c.
# Użyj instrukcji readline() i write()).

# a = int(input("Podaj niewiadomą a: "))
# b = int(input("Podaj niewiadomą b: "))
# c = int(input("Podaj niewiadomą c: "))
# wynik = a**b+c
# print(wynik)
########################################################################################################
# Zad 6.
# Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa.
# W zależności od wyniku wyświetl odpowiedni komunikat. Użyj zagnieżdżeń.

# a = int(input("Podaj liczbę a: "))
# b = int(input("Podaj liczbę b: "))
# c = int(input("Podaj liczbę c: "))
# if a > b and a > c:
#     print("Liczba a jest największa")
# elif b > a and b > c:
#     print("Liczba b jest największa")
# elif c > a and c > b:
#     print("Liczba c jest największa")
# else:
#     print("Liczby są sobie równe")
########################################################################################################
# Zad 7.
# Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float.
# Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.

# lista = [2, 3.5, 9, 5, 4.2, 12.3]
# for a in lista:
#     print(a**2)
########################################################################################################

