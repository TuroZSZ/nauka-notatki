### NumPy


###&&&___^___&&&### NumPy Array Indexing
# Indeksowanie tablicy jest takie samo, jak uzyskiwanie dostępu do elementu tablicy.
# Dostęp do elementu tablicy można uzyskać, odwołując się do jego numeru indeksu.
# Indeksy w tablicach NumPy zaczynają się od 0, co oznacza, że ​​pierwszy element ma indeks 0, a drugi ma indeks 1 itd.

# Zwróć pierwszy element szyku:
import numpy as np
arr = np.array([1,2,3,4])
print(arr[0])

# Zwróć trzeci i czwarty element i dodaj je:
import numpy as np
arr = np.array([1,2,3,4])
print(arr[2] + arr[3])

### Access 2-D Arrays
# Aby uzyskać dostęp do elementów z tablic 2-D, możemy użyć liczb całkowitych oddzielonych przecinkami, reprezentujących wymiar i indeks elementu.
# Pomyśl o tablicach 2-D jak o tabeli z wierszami i kolumnami, gdzie wymiar reprezentuje wiersz, a indeks reprezentuje kolumnę.

import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("2nd element on 1st row: ", arr[0,1])

# podobnie: piąty element drugiej kolumny to: print(arr[1,4])

# Dla access 3-D arrays wszystko wygląda tak samo:
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2]) 

# tak samo jak w przypadku innych możliwości indeksowania, tak samo tutaj możemy zastosować negative indexing:

print(arr[1, -1])

###&&&___^___&&&### NumPy Array Slicing
# Krojenie w Pythonie oznacza przenoszenie elementów z jednego podanego indeksu do innego podanego indeksu.
# Podajemy plasterek zamiast indeksu w ten sposób: [start:end].
# Możemy również zdefiniować krok w ten sposób: [start:end:step].
# Jeśli nie przejdziemy startu, przyjmuje się, że wynosi 0
# Jeśli nie przekroczymy end rozważanej długości tablicy w tym wymiarze
# Jeśli nie przejdziemy kroku, uważa się go za 1

# elementy o indeksie od 1 do 5:

import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])

# od indeksu 4 do końca szyku:
print(arr[4:])

# do indeksu 4 (bez niego)
print(arr[:4])

# podobnie sprawa wygląda w negative slicing:
print(arr[-3:-1])

### Step of slicing
# Wartość step determinuje sposób wyciągania danych:
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2]) # wyjście: [2, 4]\
# aby wybrać co drugi ze wszystkich, wpisujemy to w sposób następujący (bez parametrów oprócz step):

print(arr[::2])

### Slicing 2-D Arrays
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4]) # wyjście: [7,8,9]

# z obu elementów drugi indeks:
print(arr[0:2, 2]) # wyjście: [3 8]

###&&&___^___&&&### NumPy Data Types
# NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.
# Below is a list of all data types in NumPy and the characters used to represent them.

#     i - integer
#     b - boolean
#     u - unsigned integer
#     f - float
#     c - complex float
#     m - timedelta
#     M - datetime
#     O - object
#     S - string
#     U - unicode string
#     V - fixed chunk of memory for other type ( void )

### Checking the Data Type of an Array
# Aby sprawdzić data type szyku, możemy użyć komendy dtype
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.dtype) # wyjście: int64

import numpy as np
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype) # wyjście: <U6

### Creating Arrays With a Defined Data Type











