###&&&___^___&&&### Pandas Introduction
# Co to jest Pandas?
# Pandas to biblioteka Pythona używana do pracy ze zbiorami danych.
# Posiada funkcje analizowania, czyszczenia, eksplorowania i manipulowania danymi.

# Pandy pozwalają nam analizować duże zbiory danych i wyciągać wnioski w oparciu o teorie statystyczne.
# Pandy mogą oczyścić niechlujne zestawy danych i sprawić, że będą czytelne i istotne.
# Odpowiednie dane są bardzo ważne w nauce danych.

# Data Science: to dziedzina informatyki, w której badamy, jak przechowywać, wykorzystywać i analizować dane w celu uzyskania z nich informacji.

# Pandy udzielają odpowiedzi na temat danych. Takie jak:
#     Czy istnieje korelacja między dwiema lub większą liczbą kolumn?
#     Jaka jest wartość średnia?
#     Maksymalna wartość?
#     Wartość minimalna?
# Pandy mogą również usuwać wiersze, które nie są istotne lub zawierają nieprawidłowe wartości, takie jak wartości puste lub NULL. Nazywa się to czyszczeniem danych.

# Przykład zastosowania:

import pandas as pd
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)

print(myvar)

# Sprawdzanie wersji: 
import pandas
print(pandas.__version__)

###&&&___^___&&&### Pandas Series
# Co to jest seria?
# Seria Pandy przypomina kolumnę w tabeli.
# Jest to jednowymiarowa tablica przechowująca dane dowolnego typu.

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# Wyjście:
#  cars  passings
# 0    BMW         3
# 1  Volvo         7
# 2   Ford         2

### Labels
# Jeśli nie określono inaczej, wartości są oznaczone numerem indeksu. Pierwsza wartość ma indeks 0, druga wartość ma indeks 1 itd.
# Za pomocą tej etykiety można uzyskać dostęp do określonej wartości.

# przykład : zwróć pierwszą wartość serii:
print(myvar[0])

### Create labels
# With the index argument, you can name your own labels.
# stworzenie etykiety:
import pandas as pd
a = [1,7,2]

myvar = pd.Series(a,index = ["x","y","z"])
print(myvar)

# wyjście:
# x    1
# y    7
# z    2
# dtype: int64

# Po utworzeniu etykiet można uzyskać dostęp do elementu, odwołując się do etykiety.
# Zwróć wartość y:
print(myvar["y"])

### Key/Value Objects as Series:
# Podczas tworzenia serii możesz także użyć obiektu klucza/wartości, takiego jak słownik.
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

# Uwaga: Klucze słownika stają się etykietami.
# Aby wybrać tylko część pozycji ze słownika, użyj argumentu indeksu i określ tylko te pozycje, które chcesz uwzględnić w Serii.

# Przykład: stwórz serię z danych "day1" i "day2":
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories,index = ["day1","day2"])
print(myvar)

### Data frames
# Zestawy danych w Pandach to zazwyczaj wielowymiarowe tabele, zwane DataFrames.
# Seria jest jak kolumna, DataFrame to cała tabela.

# Przykład: stwórz DataFrame z dwóch serii:
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)

print(myvar)
# z powyższych danych powstanie tabela.

###&&&___^___&&&### Pandas DataFrames
# Pandas DataFrame to dwuwymiarowa struktura danych, podobna do dwuwymiarowej tablicy lub tabeli z wierszami i kolumnami.

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# wczytanie danych do obiektu DataFrame:
df = pd.DataFrame(data)
print(df)
# wyjscie: tabela z powyższych danych.

### Locate Row
# do lokalizacji jednego lub więcej wierszy używamy komendy loc:
print(df.loc[0]) # takie samo działanie jak indeksy. W tym wypadku print zwraca pojedynczy wiersz czyli "series"

# dwa wiersze:
print(df.loc[[0, 1]])
# Uwaga: w przypadku użycia [] wynikiem jest ramka danych Pandas.

### Named Indexes
# Za pomocą argumentu indeksu możesz nazwać własne indeksy.
# Przykład:
# Add a list of names to give each row a name:
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

### Locate Named Indexes
# Use the named index in the loc attribute to return the specified row(s). 
print(df.loc["day2"])

### Load Files Into a DataFrame
# Jeśli Twoje zestawy danych są przechowywane w pliku, Pandy mogą załadować je do DataFrame.

# Przykład: załadowanie pliku csv do DataFrame:
import pandas as pd
df = pd.read_csv('data.csv')












