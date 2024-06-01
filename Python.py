# Python nie określa zmiennych - sami musimy to zrobić.

# Jeśli chcesz sprecyzować rodzaj danych mozna to zrobić na przykład tak.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

# for integers
print(float(10))

# for floats
print(float(11.22))

# for string floats
print(float("-13.33"))

# for string floats with whitespaces
print(float("     -24.45\n"))

# string float error
# print(float("abc"))

# wartości tekstowych takich jak "abc" nie da się potraktować przez float

# PRzy użyciu funkcji type() możemy określić rodzaj danych.
x = 5
y = "John"
z = 5.75
print(type(x))
print(type(y))
print(type(z))

# na wyjściu otrzymujemy:
# <class 'int'>
# <class 'str'>
# <class 'float'>

# W pythonie nie ma znaczenia czy wartość jest w cudzysłowiu pojedynczym czy podwójnym.
# Znaczenie mają jednak małe i wielkie litery w zmiennych: a i A to nie będzie to samo. 
# Zmienne w pythonie mogą zawierać jedynie litery, cyfry i podkreślniki. Nie mogą to być słowa kluczowe pythona
# i nie mogą rozpoczynać się od cyfr.

# many values to multiple variables - wiele wartości do wielu zmiennych:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# one value to multiple variables:
c = b = n = "Orange"
print(c)
print(b)
print(n)

# Lista kilku zmiennych może trafić pod jedną wspólną:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Wyjście zmiennych:
# Aby wyświetlić wartości zmiannych używamy standardowo komendy print()

y = "Python is awesome"
print(y)

# Możliwe jest wyświetlenie kilku wymienionych zmiennych:
a = "Python"
b = "is"
c = "awesome"
print(a, b, c)
# Aby łączyć zmienne (np. tekstowe) można również użyć znaków "+" zamiast przecinków w wymienionych zmiennych w print. 
# W przypadku wartości liczbowych znak "+" doda zmienne do siebie.
# W komendzie print pojawi się błąd, jeśli spróbujemy dodać do siebie tekst (string) i wartość liczbową.

# Zmienne globalne
# Ten rodzaj zmiennych charakteryzuje się tym, że może zostać użyty w funkcji jak i poza nią. 
# Tworzenie:
w = "awesome"

def myfunc():
  print("Python is " + w)

myfunc() 

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# The global Keyword

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

# Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

# Jeśli myfunc() byłoby z tabem (pod definicją) to komenda print weźmie ogólną zmienną x = "awesome", 
# ponieważ x="fantasic" będzie wewnętrzną.

# Python data types
# Istnieją wbudowane typy danych dla Pythona:

text type = str
numeric types = int, float, complex
sequence types = list, tuple, range
mapping type = dict
set types = set, frozenset
boolean type = bool
binary types = bytes, bytearray, memoryview
none type = NoneType

# Aby otrzymać informacje o typie danych, używamy komendy print(type())
# Przykłady użycia:

x = "dostanę nową, dobrą pracę"   - str
x = 20 - int
x = 8000.48 - float
x = 23j - complex
x = ["zielone", "żółte", "czarne"]     - list
x = ("zielone", "żółte", "czarne")     - tuple
x = range(6)                - range
x = {"name" : "John", "age" : 36}       - dict
x = {"apple", "banana", "cherry"}       - set
x = frozenset({"apple", "banana", "cherry"})
x = True              - bool
x = b"Hello"          - bytes
x = bytearray(5)      - bytearray
x = memoryview(bytes(5))    - memoryview
x = None  -   NoneType

Aby ustawić typ danych należy dodać oznaczenie przed nawiasem, typu:
  
x = str("dostanę lepszą pracę")
x = int(8000)
x = float(45.21)
x = bool(5)
x = dict(name="John", age=36)

# Trzy typy numeryczne w pythonie to: int, float, complex.
# Określona zmienna jest tworzona gdy przyporządkujesz jej wartość:

x = 1       # int
y = 2.8     # float
z = 1j      #complex

# Weryfikacja odbywa się poprzez znaną funkcję type()

print(type(x))
print(type(y))
print(type(z))

# Int / integer - liczba całkowita, dodatnia lub ujemna bez wartości dziesiętnych, o nieograniczonej liczbie cyfr.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float - floating point number - liczba dodatnia lub ujemna o jednym lub więcej przecinków (kropek)
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
# Float obejmuje także liczby naukowe takie jak "e".

# Complex - liczby zespolone w których "j" reprezentuje część urojoną.
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Konwersja typów - można wykonać przekształcenie jednego typu w drugi:
x = 4    # int
y = 12.7  # float
z = 7j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)    # wynik 4.0
print(b)    # wynik 12    
print(c)    # wynik (4+0j)

print(type(a))
print(type(b))
print(type(c))
# Niemożliwe jest przekonwertowanie liczby zespolonej (complex) na float lub int.

# Liczby losowe - python nie posiada funkcji liczb losowych, tylko ma wbudowany moduł, który trzeba zaimportować przed działaniem:

import random
print(random.randrange(1,10))

# Określenie typu zmiennej - czasem dochodzi do sytuacji, że z góry chcemy określić rodzaj zmiennej. 
# Można to zrobić poprzez:

int()       # tworzy liczbę całkowitą z innej liczby, z liczby dziesiętnej (zaokrągla) lub z wartości słownej np. "342"
# Przykłady:
x = int(1)          # x will be 1
y = int(2.8)        # y will be 2
z = int("3")        # z will be 3

float()     # tworzy liczbę dziesiętną z liczb całkowitych i z wartości string (tekst) - jeśli to możliwe, 
# tj. jeśli wartość str przedstawia liczbę.
# Przykłady:
x = float(1)        # x will be 1.0
y = float(2.8)      # y will be 2.8
z = float("3")      # z will be 3.0
w = float("4.2")    # w will be 4.2

str()       #  tworzy wartość tekstową z przeróżnych typów danych, włączając inne str, int czy float.
# Przykłady:
x = str("s1")       # x will be 's1'
y = str(2)          # y will be '2'
z = str(3.0)        # z will be '3.0'


# Python strings - ciąg znaków w pythonie można zapisywać przy użyciu pojedynczych lub podwójnych cudzysłowów. 
# Dodawanie ciągu znaków do zmiennej odbywa się "klasycznie":

x = "kasa" # to to samo co 'kasa'
a = "kasa"
print(a)

# W przypadku str wielowierszowych zapisujemy je przy użyciu trzech cudzysłowów- pojedynczych lub podwójnych:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Przy takim przedstawieniu, w rezultacie otrzymamy dokładnie takie samo formatowanie tekstu jak w kodzie. 

# Strings are Arrays (szyki)
# Python nie ma określonego typu danych dla liter. Pojedyncza litera to string o długości 1.

# Przykład jak "wydobyć" daną literę.
a= "Hello, World!"
print(a[1])


# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Długość ciągu określamy komendą len() (od lengh):

c = "dostanę nową pracę"
print(len(c))

# Check String
# Aby sprawdzić, czy zadana fraza znajduje się w zdaniu wykorzytujemy słowo-klucz "in". Przykład:
txt = "THe best things in life are free!"
print("free" in txt)

# Wyjście - True/False. Możliwe jest też stworzenie warunków:
txt = "THe best things in life are free!"
if "free" in txt:
  print("To słowo jest obecne w zdaniu")
else:
  print("Nie ma tego")

# W przypadku, gdy sprawdzamy, że danego słowa czy frazy nie ma w zdaniu:

txt = "Dostanę dobrą robotę z dobrą płacą."
print("słabo" not in txt)
# Wyjście true/false. Tak samo możemy zastosować warunki.
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


# Python - Slicing Strings

# Można wyodrębnić fragment ciągu znaków na postawie numerów znaków:

b = "Hello, world"
print(b[2:6]) 
#pierwszy znak ma indeks 0.

#slice from the start - from start to position 5,

print(b[:5])

#analogicznie slice do the end:

print(b[4:])

#negative indexing - wyświetlanie znaków w odwrotnej kolejności

print(b[-8:-2])

# Python - modify strings
# wielkie lub małe znaki ciągu - upper/lower case

c = "    Wiedźmin Geralt   "
print(c.upper())
print(c.lower())

#remove whitespace - usuwa nadmiarowe spacje z początku lub końca.

print(c.strip())

#replace string - funkcja replace():

print(c.replace("W", "C"))

#split string 

d = "Kaer Morhen"
print(d.split(" "))

# string concatenation (powiązać)
a = "Kaer"
b = "Morhen"
c = a+b
print(c)

#przykład: dodanie spacji:
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Python - format - strings
# jak już nauczyłem się wcześniej, nie można do siebie dodawać wartości tekstowych i liczbowych "tak po prostu"
# można jednak to zrobić używając formuły format(). Ta formuła formatuje wartość i umiejscawia ją w miejscu nawiasów {}
age = 36
txt = "I'm John and I am {}"
print(txt.format(age))

# {} przyjmuje nielimitowaną ilość argumentów i umieścić je w kilku miejscach. Na przykład:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Możliwe jest także poindeksowanie numerów, aby mieć pewność, że znajdą się we właściwym miejscu.
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#wyjście: I want to pay 49.95 dollars for 3 pieces of item 567 

# Python escape characters
# Aby użyć znaków których normalnie nie da się wstawić w ciąg znaków możemy użyć "escape character". W przypadku zdania:
txt = "We are the so-called "Vikings" from the north."
# wystąpi błąd, że nie zgadzają się cudzysłowy. Dlatego:
txt = "We are the so-called \"Vikings\" from the north."

# Inne przykłady to:
# \' - single quote
# \\  backslash
# \n  new line
# \r  carrage return
# \t tab
# \b  backspace (usuwa znak w wyznaczonym miejscu)
# \f form feed



Warning ################# STRING METHODS ###########################
# All string methods return new values. They do not change the original string.

# capitalize()	Converts the first character to upper case
txt = "okolice warowni wiedźminów zapierają dech w piersiach." 
print(txt.capitalize()) # lub x = txt.capitalize() wówczas print(x)

# casefold()	Converts string into lower case
txt2 = "Czas Białego Zimna"
x = txt2.casefold()
print(x)

# center()	Returns a centered string - print the word "Skellige" taking up the space of 30 characters with "Skellige" in the middle.
txt3 = "Skellige"
print(txt3.center(30))
# możemy też dodać inny znak niż spacja: vvvvvvvvvvvSkelligevvvvvvvvvvv
print(txt3.center(30, "v"))

#_____|_#_|_# count() - zwraca info, ile razy żądana wartość wystąpiła w tekście.
txt4 = "I love apples, apple is my favorite fruit."
x=txt4.count("apple")
print(x)

# LUB
print(txt4.count("apple"))

# jeśli chcemy szukać wartości w podanym przedziale znaków:
print(txt4.count("apple", 10, 24))

#_____|_#_|_# encode() - formułą dekoduje ciąg na określony sposób. Bez określenia encode program użyje UTF-8.
txt = "My name is Ståle"
x = txt.encode()
print(x) # wyjście: b'My name is St\xc3\xe5le' 

#_____|_#_|_# endswith() - zwraca True jeśli ciąg będzie kończył się zadaną wartością:
txt5="Redania sprawuje nadzór nad Novigradem."
print(txt5.endswith("Novigradem.")) #wyjście - true
#możliwy jest wariant tej funkcji z określeniem miejsc/znaków w ciągu:
print(txt5.endswith("Novigradem.", 20, 30)) # wyjście - false.

#_____|_#_|_# expandtabs() - ustanawia ilość spacji w danym miejscu wedle parametru.
txt6="N\ti\tl\tf\tg\ta\ta\tr\td\t"  # Nilfgaard
print(txt6.expandtabs(4))  # wyjście: N   i   l   f   g   a   a   r   d


#_____|_#_|_# count() - zwraca info, ile razy żądana wartość wystąpiła w tekście.
txt4 = "I love apples, apple is my favorite fruit."
x=txt4.count("apple")
print(x)

# LUB
print(txt4.count("apple"))

# jeśli chcemy szukać wartości w podanym przedziale znaków:
print(txt4.count("apple", 10, 24))

#_____|_#_|_# encode() - formułą dekoduje ciąg na określony sposób. Bez określenia encode program użyje UTF-8.
txt = "My name is Ståle"
x = txt.encode()
print(x) # wyjście: b'My name is St\xc3\xe5le' 

#_____|_#_|_# endswith() - zwraca True jeśli ciąg będzie kończył się zadaną wartością:
txt5="Redania sprawuje nadzór nad Novigradem."
print(txt5.endswith("Novigradem.")) #wyjście - true
#możliwy jest wariant tej funkcji z określeniem miejsc/znaków w ciągu:
print(txt5.endswith("Novigradem.", 20, 30)) # wyjście - false.

#_____|_#_|_# expandtabs() - ustanawia ilość spacji w danym miejscu wedle parametru.
txt6="N\ti\tl\tf\tg\ta\ta\tr\td\t"  # Nilfgaard
print(txt6.expandtabs(4))  # wyjście: N   i   l   f   g   a   a   r   d

#_____|_#_|_# find() - szukanie określonej wartości - zwraca pozycję, gdzie została znaleziona.
txt7 = "W świecie Wiedźmina jest wiele królestw: Temeria, Kovir i Poviss, Redania, Kaedwen, Cintra itd."
print(txt7.find("Redania"))

#_____|_#_|_# format() - wstawia żądaną wartość w nawiasie {}. Można definiować więcej wartości i ustawiać je wedle naszej kolejności.
txt8 = "For only {price:.2f} pounds!"
print(txt8.format(price=49))

                # Inny przykład
t1 = "Mam na imię {imie}, mam {wiek} lata".format(imie="Kasia", wiek = 24)
t2 = "Mam na imię {0}, mam {1} lata".format("Kasia",24)
t3 = "Mam na imię {}, mam {} lata".format("Kasia",24)
print(t1)
print(t2)
print(t3)
            # formatować można naróżne sposoby, zarówno pod kątem tekstowym jak i liczbowym. 
            # najlepiej jest wyszukiwać "formatting types python"

#_____|_#_|_# index() - wyszukuje ciąg o określonej wartości i wskazuje jego położenie (położenie TYLKO pierwszego wyniku).
print(txt.index("e")) # wyjście - 6

    # mozliwe jest też określenie zakresu:
print(txt.index("e",10,40))

    # jeśli wartość nie zostanie znaleziona, to funkcja find() zwróci -1, a index() zwróci błąd.
    # print(txt7.find("x"))
    # print(txt7.index("x"))

#_____|_#_|_#



================================================================================


#_____|_#_|_# 


########## Python Booleans - boolean reprezentuje jedynie dwa stany - prawda lub fałsz (true/false). 
# Wartość bool pojawi się np. przy porównywaniu:
print(10>9) 
print(12==11)
print(10<9)

### Evaluate values and variables - sprawdzanie wartości i zmiennych jest możliwe przy pomocy funkcji bool():

print(bool("Pontar"))
print(bool(24))

#variables:
v = "Pontar"
n = 24

print(bool(v))
print(bool(n))

print(        )

### most values are True - większość wartości to prawda. 
# any string is true
# any number, except 0, is true
# any list, tuple, set and dictionary are True, except empty ones
# następujące formuły wskażą True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

### some values are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# Jeszcze jedna wartość, w tym przypadku obiekt, ma wartość False i dzieje się tak, 
# jeśli masz obiekt utworzony z klasy z funkcją __len__, która zwraca 0 lub False:

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

# Functions can return a boolean - można stworzyć funkcje które zwrócą prawdę lub fałsz w zależności od warunków:
def myfunction():
    return True
print(myfunction())

# można dzięki wartościom prawda/fałsz inicjować inne funkcje:
def myfunction():
    return False

if myfunction():
    print("Oj tak")
else:
    print("Oj nie")
    
# niektóre funkcje mają wbudowany bool i zwracają True/False w zależności od wyniku. Np. isinstance(), 
# czyli funkcja która określa czy dane są konkretnego typu:
q = 400
w = "Jaruga"
print(isinstance(q, int)) #True
print(isinstance(w, int)) #False
print(isinstance(w, str)) #True
print(isinstance(q, float)) #False

#&&&&#&&&&# Python operators - operatory są używane do dokonywania operacji na wartościach i zmiennych.
# Istnieją następujące typy operatorów:
    # Arithmetic:
        # + (addition), - (substraction), * (multiplication), / (division), % (modulus), ** (exponentiation-potęgowanie), // (floor division-integer division-podaje liczbę całkowitą dzielenia bez tego co jest po przecinku)
    
    # Assignment:
        # = 
        # +=
        # -=
        # *=
        # /=
        # %=
        # //=
        # **=
        # &=
        # |=
        # ^=
        # >>= i <<=
        
    # Comparison:
        # == (equal), != (not equal), >, <, >=, <=
        
    # Logical
        
    # Identity
    # Membership
    # Bitwise
    
  # Logical:
        # AND, OR, NOT
        
    # Identity
        # is, is not
    # Membership
        # in, not in
    # Bitwise
    
### precedence order - kolejność ważności operatorów

#&&&#&&&# Python lists - listy to sposób na zawarcie większej ilości danych w jednej zmiennej. 
# pozostałe typy, które przechowują więcej danych w jednej zmiennej to: tuple, set, dictionary.

# przykład listy:

lista_wiedźminów = ["Vesemir", "Geralt", "Ciri"]
print(lista_wiedźminów)

# pierwszy element z listy posiada indeks [0], kolejny [1] itd. Możliwe jest dodawanie takich samych wartości, 
# oraz dodawanie/usuwanie elementów po utworzeniu listy.

#list length - determine how many items a list has.
print(len(lista_wiedźminów)) #wyjście - 3

# listy mogą zawierać dowolne typy danych: str, float, bool itd.
# jedna lista może zawierać różne typy danych naraz. 
wartosci = ["Gors Velen", 45, True, 12, "Temeria", 12.75]

# Można sprawdzać typ danych przy użyciu type():
print(type(lista_wiedźminów)) # <class 'list'>

# do stworzenia listy można wykorzystać funkcję list(). Co istotne, występują tu podwójne nawiasy:
planety = list(("Uran", "Neptun", "Jowisz"))
print(planety)

# Kolekcje Pythona (arrays/szyki)

# W języku programowania Python istnieją cztery typy danych kolekcji:

#     List - to zbiór uporządkowany i zmienny. Zezwala na zduplikowanych członków.
#     Tuple - to zbiór uporządkowany i niezmienny. Zezwala na zduplikowanych członków.
#     Set (zestaw) - to kolekcja, która jest nieuporządkowana, niezmienna* i nieindeksowana. Żadnych zduplikowanych członków.
#     Dictionary - to zbiór uporządkowany** i podlegający zmianom. Żadnych zduplikowanych członków.
        # *Set items are unchangeable, but you can remove and/or add items whenever you like.




#&&&#&&&# Python access list items - listy są zindeksowane i można wykorzystywać je/umiejscawiać przy pomocy indeksu:
krainy = ["Temeria", "Redania", "Nilfgaard", "Cintra"]
print(krainy[2])  # pamiętamy, że pierwszy element ma indeks [0]

### negative indexing - czyli zaczynanie od końca. -1 to ostatni element, -2 przedostani itd.
print(krainy[-1]) # Cintra

# tak samo działa zakres - jak w wypadku znaków w ciągu we wcześniejszych modułach:
print(krainy[1:3]) # zakres działa tak, że zaczyna się od 1 ale kończy się przed 3 - <1:2)

# zapis [:3] pozwala na wyznaczenie elementów do "Cintry" (jednak BEZ niej)
print(krainy[:3])
#podobnie zapis [1:] - tutaj jednak elementy będą liczone od "Redanii":
print(krainy[1:])

#podobnie indeksy negatywne:
print(krainy[-3:-1]) # Redania i Nilfgaard

# check if item exists:
if "Cintra" in krainy:
    print("Tak, Cintra jest na liście")
    
    
#&&&#&&&# CHANGE LIST ITEMS - aby zmienić wartość na liście, musimy to zrobić używając indeksu tego, co chcemy zmienić:
moje_krainy = ["Vasaro", "Rijtn", "Cesselon", "Neivaal"]
moje_krainy[1] = "Atwa"
print(moje_krainy)

### change a range of item values
moje_krainy[0:2] = ["Kyl Muir", "Yel-Dagar"] #tutaj tak samo jak wcześniej - 0 się wlicza a przed 2 się kończy.
print(moje_krainy)

# w przypadku, gdy elementów do zmiany będzie więcej niż wskazanych miejsc/indeksów, to nadmiarowe elementy zostaną dodane:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #wyjście ['apple', 'blackcurrant', 'watermelon', 'cherry']

# jednak w sytuacji, gdy wskazanych indeksów jest więcej niż wartości, to te wartości "pokryją" wszystkie miejsca.

### INSERT ITEMS - dodajemy elementy do listy przy użyciu funkcji insert()
moje_krainy.insert(0, "Atwa")
print(moje_krainy)

#&&&#&&&# ADD LIST ITEMS - aby dodać pozycję na końcu listy korzystamy z funkcji append():
moje_krainy.append("Batorfold")
print(moje_krainy)

### INSERT ITEMS - aby dodać pozycję w określonym indeksie korzystamy ze znanej już funkcji insert():
moje_krainy.insert(3, "Uragh-Podor") #indeks 3 czyli na czwartej pozycji
print(moje_krainy)

### EXTEND LIST - aby dodać jedną listę do drugiej używamy funkcji extend():
postacie = ["Cernunnos", "Farghasen", "Mael"]
postacie_2 = ["Cedric de Morga", "Hevre"]
postacie.extend(postacie_2)
print(postacie)

### ADD ANY ITERABLE - do listy można dołączyć dowolny typ tekstowy:
postacie_3 = ("Harmaszizijah", "Terienne") #typ - tuple
postacie.extend(postacie_3)
print(postacie)


#&&&____#____&&&# REMOVE SPECIFIED ITEM - funkcja remove():
postacie.remove("Farghasen")
print(postacie) #jeśli jedna wartość występuje więcej niż raz, to funkcja remove() usunie tylko pierwsze wystąpienie.

### REMOVE SPECIFIED INDEX - robimy to funkcją pop():
postacie.pop(3) #jeśli w argumencie pop() nic się nie znajdzie, to funkcja usunie ostatni element z listy.
print(postacie)

# usuwać elementy można także przy pomocy keyword "del"
del postacie[0]
print(postacie)

#przy użyciu del możemy również usuwać całą listę:
del postacie

### CLEAR THE LIST
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#&&&___#___&&&# LOOP THROUGH A LIST - funkcja "for"
thislist = thislist
for x in thislist:
  print(x)
  
# loop through the index numbers
for i in range(len(thislist)):
  print(thislist[i])

# The iterable created in the example above is [0, 1, 2].
# using a while loop
thislist = thislist
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
# looping using list comprehension
thislist = thislist
[print(x) for x in thislist]

#&&&___#___&&&# LIST COMPREHENSION
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# można to zrobić także w jednej linijce kodu:
newlist = [x for x in fruits if "a" in x]
print(newlist)

# SYNTAX
# newlist = [expression for item in iterable if codition == True]

newlist = [x for x in fruits if x != "apple"]

# the iterable can be any iterable object, like a list, tuple, set etc.
# funckcja range() do stworzenia "iterable":
newlist = [x for x in range(10)]

# zmiana wyrazów na "orange" zamiast "banana"

newlist = [x if x != "banana" else "orange" for x in fruits]
# The expression in the example above says:

# "Return the item if it is not banana, if it is banana return orange".


###&&&___#___&&&### LIST COMPREHENSION
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:
 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
        
print(newlist) #wyjście: ['apple', 'banana', 'mango']

#syntax: 
# newlist = [expression for item in iterable if condition == True]
#przykład: akceptacja tylko wyników które nie są "apple":
newlist = [x for x in fruits if x != "apple"]

#iterable
newlist = [x for x in range(10)]

newlist = [x for x in range(10) if x < 5]

#expression
newlist = [x.upper() for x in fruits]
#set all values in the new list to "hello"

newlist = ['hello' for x in fruits]

#return "orange" instead "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
# The expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange".

# LISTS

### Case Insensitive Sort - domyślnie, funkcja sort() jest zależna od wielkości liter.
# wszystkie wyniki z wielką literą będą przed wynikami z małą literą.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # wyjście: ['Kiwi', 'Orange', 'banana', 'cherry'] 

# Natomiast możemy użyć wbudowanej funkcji, która uszereguje elementy prawidłowo.
thislist.sort(key = str.lower)
print(thislist) # wyjście: ['banana', 'cherry', 'Kiwi', 'Orange'] 

### Reverse Order - aby odwrócić kolejność elementów na liście, korzystamy z funkcji reverse()
thislist = thislist
thislist.reverse()
print(thislist)

# odwrócenie kolejności po początkowym ustawieniu alfabetycznym:
thislist.sort(key = str.lower)
thislist.reverse()

print(thislist)
###&&&___#___&&&### SORT LISTS - funkcja sort() sortuje elementy listy alfanumerycznie:

bronie = ["miecz", "łuk", "kusza", "morgenstern", "topór"]
bronie.sort()
print(bronie)

liczby = [100, 50, 65, 82, 32, 44]
liczby.sort()
print(liczby)

### SORT DESCENDING (DSC) - aby odwrócić szeregowanie, należy użyć keyword argument reverse = True:
bronie = ["miecz", "łuk", "kusza", "morgenstern", "topór"]
bronie.sort(reverse = True)
print(bronie) # występuje problem z językiem polskim - łuk był na początku DSC.

### customize sort function - przy użyciu argumentu key = function
def myfunc(n):
  return abs(n - 50)
liczby = [100, 50, 65, 82, 32, 44]
liczby. sort(key = myfunc)
print(liczby)  # Sort the list based on how close the number is to 50

### case insensitive sort: - funkcja domyślna sort() jest uwarunkowana wielkością znaków, stąd wyrazy zaczynające się z wielkiej litery
# będą na początku:
thislist1 = ["banana", "Orange", "Kiwi", "cherry"]
thislist1.sort()
print(thislist1)

### reverse order - odwrócenie kolejności elementów z listy:
thislist1 = ["banana", "Orange", "Kiwi", "cherry"]
thislist1.reverse()
print(thislist1)


###&&&___^___&&&### Python Copy Lists
# nie można kopiować list poprzez proste list1 = list2, ponieważ list2 zawsze będzie się
# odwoływać do list1. Zmiany w list1 automatycznie zostaną wprowadzone do list2.
# Aby stworzyć kopię listy korzystamy z funkcji copy()

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Możliwe jest także stworzenie kopii przy pomocy list():
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

###&&&___^___&&&### Python Join Lists
# Istnieje kilka metod łączenia ze sobą list.
# Najłatwiejszy to operator "+"
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) # wyjście: ['a', 'b', 'c', 1, 2, 3] 

# Inny sposób to dodanie jednej listy do drugiej komendą append():
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:    # "tłumaczenie" - dla każdego elementu z list2
    list1.append(x)
print(list1)

# Trzecim sposobem jest użycie komendy extend():
list1.extend(list2)
print(list1)

###&&&___^___&&&### List Methods:
list.append()   # Adds an element at the end of the list
list.clear()    # Removes all the elements from the list
list.copy()     # Returns a copy of the list
list.count()    # Returns the number of elements with the specified value
list.extend()   # Add the elements of a list (or any iterable), to the end of the current list
list.index()    # Returns the index of the first element with the specified value
list.insert()   # Adds an element at the specified position
list.pop()      # Removes the element at the specified position
list.remove()   # Removes the item with the specified value
list.reverse()  # Reverses the order of the list
list.sort()     # Sorts the list

# ćwiczenia
# Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

# Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")


# ====================== SETS

###&&&___^___&&&### Python Add Set Items
# gdy zestaw został stworzony, to nie można edytować elementów, ale można je dodawać.
# Aby dodać element używamy funkcji add():

thisset = {"apple", "banana", "cherry"}
thislist.add("orange")
print(thisset)

### Add Sets
# Aby dodać elementy z jednego zestawu do drugiego, korzystamy z update():
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset) # wyjście: {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'} 

### Add Any Iterable - w komendzie update() nie musi znajdować się set - 
# może być tam dowolny obiekt iterowalny (krotka, lista, słownik)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)

###&&&___^___&&&### Python - Remove Set Items
# aby usunąć element używamy komendy remove() lub discard():
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Note: If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# Note: If the item to remove does not exist, discard() will NOT raise an error.

# Można również użyć komendy pop() natomiast usunie ona losowy element zestawu.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# Metoda clear() z kolei usunie wszystkie elementy z zestawu.
thisset.clear()
print(thisset)

# A wyrażenie del usunie set całkowicie:
del thisset
print(thisset)

###&&&___^___&&&### Python Loop Sets
# można stworzyć pętle przez elementy przez wyrażenie "for":
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
    
###&&&___^___&&&### Python - Join Sets
# Join Two Sets - istnieje kilka metod łączenia zestawów.
# Pierwszym z nich jest union() - zwraca nowy set zawierający składowe z "substratów"
# drugim zaś update() który dodaje wartości z jednego setu do drugiego.

#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1:

set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.

### Keep ONLY the Duplicates
# komenda intersection_update() zachowa jedynie elementy, które występują we wszystkich wskazanych setach:
x = {"zamek", "kłódka", "zasuwa"}
y = {"twierdza", "cytadela", "zamek"}

x.intersection_update(y)
print(x)

# sama komenda intersection() zwróci nowy set, który będzie zawierał elementy, 
# które wcześniej wystąpiły we wszystkich setach:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)

### Keep All, but NOT the Duplicates
# Komenda symmetric_difference_update() zachowa jedynie elementy, które nie występują we wszytkich setach:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x) # wyjście: {'google', 'banana', 'microsoft', 'cherry'}

# Podobnie jak w intersection, aby stworzyć nowy zestaw, który będzie zawierał jedynie wartości, 
# które nie występują we wszystkich setach użyjemy komendy symmetric_difference():

z = x.symmetric_difference(y)
print(z)

# uwaga - wartości True i 1 będą postrzegane jako duplikaty.
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z) # wyjście: {2, 'google', 'cherry', 'banana'} 

###&&&___^___&&&### Set Methods
set.add()                           # Adds an element to the set
set.clear()                         # Removes all the elements from the set
set.copy()                          # Returns a copy of the set
set.difference()                    # Returns a set containing the difference between two or more sets
set.difference_update()             # Removes the items in this set that are also included in another, specified set
set.discard()                       # Remove the specified item
set.intersection()                  # Returns a set, that is the intersection of two other sets
set.intersection_update()           # Removes the items in this set that are not present in other, specified set(s)
set.isdisjoint()                    # Returns whether two sets have a intersection or not
set.issubset()                      # Returns whether another set contains this set or not
set.issuperset()                    # Returns whether this set contains another set or not
set.pop()                           # Removes an element from the set
set.remove()                        # Removes the specified element
set.symmetric_difference()          # Returns a set with the symmetric differences of two sets
set.symmetric_difference_update     # Inserts the symmetric differences from this set and another
set.union()                         # Return a set containing the union of sets
set.update()                        # Update the set with the union of this set and others

###&&&___&___&&&### PYTHON TUPLES (krotki) - Krotki służą do przechowywania wielu elementów w jednej zmiennej.
# Tuple to jeden z 4 wbudowanych typów danych w Pythonie używanych do przechowywania kolekcji danych, 
# pozostałe 3 to Lista, Zestaw i Słownik, wszystkie o różnych właściwościach i zastosowaniu.
# Krotka to zbiór uporządkowany i niezmienny. Krotki zapisuje się w nawiasach okrągłych.
# tworzenie krotki (tuple)
mytuple = ("jagoda", "porzeczka", "agrest")
print(mytuple)

### TUPLE ITEMS- elementy w krotce są indeksowane od 0, drugi element to [1] itd.
# ORDERED - krotki mają zdefiniowane uszeregowanie i to uszeregowanie nie zmienia się.

# UNCHANGEABLE - krotek nie da się zmienić - nie można dodać ani usunąć elementów w stworzonej krotce.

# ALLOW DUPLICATES - elementy krotki mają indeksy, tak więc 

# TUPLE LENGTH - długość krotki - ilość elementów - sprawdzamy przy użyciu komendy len():
print(len(mytuple))

# ONE ITEM TUPLE - generalnie python nie dopuszcza istnienia krotki z jednym elementem, natomiast można to obejść 
# dodając przecinek po jedynej wartości krotki:
tuptuptuple = ("apple",)
print(type(tuptuptuple))

# TUPLE ITEMS - DATA TYPES - elementy krotki mogą być dowolnym typem - string, integers, boolean itd.
tuple1 = ("abc", 34, True, 40, "male")

# TUPLE TYPE() - typ tuple przy użyciu komendy sprawdzającej "type" wyświetli się jako <class 'tuple'>

# THE TUPLE CONSTRUCTOR - jest możliwe użycie komendy tuple() do stworzenia krotki:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) 

###&&&___^___&&&### Python Access Tuple Items - można uzyskać dostęp do elementów krotki, odwołując się do numeru indeksu:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

### Negative indexing - -1 refers to last item, -2 to the second last item etc.

print(thistuple[-1]) # wyjście: cherry

### Range of indexes - tak jak w przypadku list, można wyciągnąć obiekty z zakresu:
# zwróć trzeci, czwarty i piąty obiekt
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # The search will start at index 2 (included) and end at index 5 (not included).

# jeśli zostawimy puste przed : w zakresie, to wybierze elementy od początku:
print(thistuple[:4]) # czyli elementy 0,1,2,3 bez 4 (kiwi)
# taka sama zasada dotyczy w drugą stronę: od danej pozycji do końca.

### Range of Negative Indexes - specify negative indexes if you want to start search
# from the end of the tuple:
# This example returns the items from index -4 (included) to index -1 (excluded)
print(thistuple[-4:-1]) # wyjście: ('orange', 'kiwi', 'melon')

### Check if Item Exists - To determine if a specified item is present in a tuple use the in keyword:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Ta, jabłko jest wśród nas")

###&&&___^___&&&### Python Update Tuples
# krotki są niezmienialne - nie można zmienić, dodać czy usunąć elementów stworzonej krotki.

### Change Tuple Values - aby zmienić wartości w krotce musimy zrobić obejście.
# w pierwszym kroku konwertujemy krotkę w listę, zmieniamy wartości i rekonwertujemy na krotkę:
owoce = ("poziomka", "agrest", "pigwa")
y = list(owoce)
y[1] = "porzeczka"
owoce = tuple(y)
print(owoce)

### Add Items - analogicznie jak przy zmianach:
samochody = ("VW", "Jaguar", "BMW")
z = list(samochody)
z.append("Volvo")
samochody = tuple(z)

# możliwe jest jednak łączenie krotek ze sobą:
samochody_plus = ("Mercedes", "Mitsubishi")
samochody += samochody_plus
print(samochody)

# Note: When creating a tuple with only one item, remember to include a comma 
# after the item, otherwise it will not be identified as a tuple.

### Remove Items
# nie można usuwać elementów w krotce. Usuwanie odbywa się podobnie co dodawanie.
thistuple = ("apple", "banana", "cherry")
y =list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# całkowite usunięcie krotki:
del thistuple
print(thistuple)  #this will raise an error because the tuple no longer exists 

###&&&___^___&&&### Python Unpack Tuples
# unpacking a tuple - gdy tworzymy krotkę, przyporządkowujemy wartości normalnie. Nazywa się to "packing" tuple.
# packing
owoce = ("poziomka", "morela", "truskawka")
# w pythonie możliwy jest "unpacking" czyli wyciągnięcie wartości z krotki w zmienne:
(val1, val2, val3) = owoce

print(val1) # wyjście - poziomka
print(val2) # wyjście - morela
print(val3) # wyjście - truskawka

#Uwaga: liczba zmiennych musi odpowiadać liczbie wartości w krotce; 
# w przeciwnym razie należy użyć gwiazdki, aby zebrać pozostałe wartości w formie listy.

### Using Asterisk* - If the number of variables is less than the number of values, 
# you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# wyjście:
# apple
# banana
# ['cherry', 'strawberry', 'raspberry']

# Jeśli gwiazdka zostanie dodana do innej nazwy zmiennej niż ostatnia, Python będzie przypisywał wartości do zmiennej, 
# aż liczba pozostałych wartości będzie równa liczbie pozostałych zmiennych.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# wyjście: 
# apple
# ['mango', 'papaya', 'pineapple']
# cherry

###&&&___^___&&&### Loop Tuples
# Loop Through a Tuple
# iteracja przez elementy przy pomocy pętli for:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

### Loop Through the Index Numbers
# można iterować przy pomocy pętli na podstawie indeksów obiektów w krotce:
# użyjmy range() i len() do stworzenia odpowiedniej iteracji:
# print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)): 
    print(thistuple[i])

# range to zakres elementów - natomiast wymaga on wartości liczbowej.
# wartość liczbową otrzymujemy poprzez zliczenie elementów krotki.

### Using a While Loop
# możliwe jest również pętlowanie przez pętle while.
# funkcja len() determinuje długość krotki, a pętla rozpoczyna się od 
# od pozycji 0 i przechodzi przez wskazane elementy - tutaj akurat co jeden.
thistuple = thistuple
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

###&&&___^___&&&### Python - Join Tuples
# Aby dodać dwie lub więcej krotek stosujemy operator +
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) # wyjście: ('a', 'b', 'c', 1, 2, 3) 

### Multiply Tuples
# aby pomnożyć krotkę używamy operatora *:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) # wyjście: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

###&&&___^___&&&### Python - Tuple Methods
# python posiada dwie wbudowane funkcje do działania na krotkach:
# count() Returns the number of times a specified value occurs in a tuple
# index()   Searches the tuple for a specified value and returns the position of where it was found
# Przykłady:
owoce = ("poziomka", "morela", "agrest", "pigwa", "morela", "porzeczka")

print(owoce.count("morela")) # 2

print(owoce.index("porzeczka")) # 5
print(owoce.index("morela")) # 1 (pokazuje tylko pierwsze wystąpienie)


###&&&___#___&&&### PYTHON SETS
# Zestawy służą do przechowywania wielu elementów w jednej zmiennej.
# Set to jeden z 4 wbudowanych typów danych w Pythonie używanych do przechowywania kolekcji danych. Pozostałe 3 to List, Tuple i Dictionary, każdy z nich ma inną jakość i zastosowanie.
# Zbiór to zbiór, który jest nieuporządkowany, niezmienny* i nieindeksowany.
# * Uwaga: Ustawionych elementów nie można zmieniać, ale można usuwać elementy i dodawać nowe
# zestawy są pisane w {} nawiasach.

# stworzenie zestawu
thisset = {"rzeki", "góry", "jeziora"}
print(thisset) # set nie jest uporządkowany, więc nie można być pewnym zwróconego szeregowania.
# set - nie można duplikować wartości
# True i 1 są rozpoznawane jako jedna wartość. Tak samo False i 0.
# W przypadku wystąpienia duplikatów w zestawie, to jest odczytywany tylko jeden.

### Get the Length of a Set - funkcja len()
print(len(thisset))

###&&&___^___&&&### Python Access Set Item
# Nie można uzyskać dostępu do elementów zestawu poprzez odwoływanie się do indeksu lub klucza.
#cMożna jednak przeglądać elementy zestawu za pomocą pętli for lub pytać, czy w zestawie znajduje się określona wartość, używając słowa kluczowego in.

### Set Items Data Types - w zestawie mogą być dowolne dane:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {True, 3, "mhm", 7, False}

### Set - type() - tą komendą sprawdzamy klasę danych:
print(type(set4))

### The set() Constructor - można tworzyć zestaw funkcją set():
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 

# loop through the set and print the values
thisset = {"apple", "banana", "cherry"}
for x in thissheet.pl:
  print(x)
  
### Sprawdzimy w jaki sposób można się skontaktować.
# Sprawdzenie, że banana występuje tylko w scenie garnkowej.

# sprawdź czy  banana wkurza. 
thisset = thisset
thisset = {""}

vthisset = {"apple", "banana", "cherry"}











# Python Collections (Arrays)

# There are four collection data types in the Python programming language:

#     List is a collection which is ordered and changeable. Allows duplicate members.
#     Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#     Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#     Dictionary is a collection which is ordered** and changeable. No duplicate members.

###



###&&&___^___&&&### PYTHON DICTIONARIES - dictionaries (słowniki) są używane do przechowywania danych w kluczu: para wartości.
# Słowniki od wersji Python 3.7 są uporządkowane (wcześniej było odwrotnie), można je zmieniać ale nie mogą posiadać zduplikowanych wartości.
# Słowniki są zapisywane w nawiasach {}, mają klucze i wartości.

# przykład: 
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
print(thisdict)

### DICTIONARY ITEMS
# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# przykład: print the "brand" value of the dictionary:
print(thisdict["brand"])

### ORDERED OR UNORDERED?
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

### CHANGEABLE
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

### DUPLICATES NOT ALLOWED - nie mogą występować dwa elementy z tym samym kluczem:
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) 

### DICTIONARY LENGTH - To determine how many items a dictionary has, use the len() function:
print(len(thisdict))

### DICTIONARY ITEMS - DATA TYPE - ANY TYPE - boolean, integer, string, list, tuckle itd.
# standardowo można sprawdzić typy wartości funkcją type():
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict)) 

### THE DICT() CONSTRUCTOR - możliwe jest stworzenie słownika używając funkcji dict():
nowydict = dict(name = "John", age = 36, country = "England")
print(nowydict)

###&&&___^___&&&### ACCESSING ITEMS - Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# Przykład - get the value of the "model" key
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] # wyjście: Mustang

# Taki sam efekt da komenda get():
x = thisdict.get("model")

### GET KEYS - komenda keys() zwróci listę wszystkich kluczy w słowniku:
x = thisdict.keys()
print(x) # wyjście: dict_keys(['brand', 'model', 'year']) 

# Dodajmy nowy klucz do słownika i sprawdźmy zmiany:
x = thisdict.keys()
print(x) # przed zmianami

thisdict["color"] = "white"
print(x) # po zmianach: dict_keys(['brand', 'model', 'year', 'color'])

### GET VALUES - komenda values() zwróci wszystkie wartości ze słownika:

x = thisdict.values()
# Możemy dzięki temu aktualizować wartości:

x = thisdict.values()

print(x) # przed zmianami

thisdict["year"] = 2020
print(x) # po zmianach

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change
car["color"] = "red"

print(x) #after the change 
# w tym wypadku linijka: car["color"] = "red" dodaje klucz i wartość.
# Możemy sprawdzić klucze:
y = car.keys()
print(y) # wyjście: dict_keys(['brand', 'model', 'year', 'color'])

### GET ITEMS - komenda items() zwróci nam każdy element słownika:

x = car.items()
print(x) # wyjście: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

### CHECK IF KEY EXISTS - aby sprawdzić, czy dany klucz jest w słowniku, użyjmy keyword "in"
thisdict = thisdict

if "model" in thisdict:
  print("Tak, model jest jednym z kluczy słownika thisdict")

###&&&___^___&&&### - CHANGE DICTIONARY ITEMS
# change values - można zmienić wartość elementu odwołując się do jego klucza:

thisdict = thisdict
thisdict["year"] = 2018

### UPDATE DICTIONARY - The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict.update({"year": 2020})

###&&&___^___&&&### ADD DICTIONARY ITEMS - dodawanie elementów do słownika odbywa się przez dodanie nowego indeksu klucza i 
# dodanie do niego wartości:
thisdict["color"] = "lime"
print(thisdict)

### UPDATE DICTIONARY - The update() method will update the dictionary with the items from a given argument. If the item does not exist, 
# the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.
# Add a color item to the dictionary by using the update() method:
thisdict.update({"color": "red"})

###&&&___^___&&&### REMOVE DICTIONARY ITEMS - jest kilka metod usuwania pozycji ze słownika.
# Przykładowo: pop() usuwa pozycję z kluczem:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) # wyjście: {'brand': 'Ford', 'year': 1964} 

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car) # wyjście: {'brand': 'Ford', 'model': 'Mustang'} 

# del keyword removes the item with the specified key name:
hisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["brand"]
print(thisdict) # wyjście: {'model': 'Mustang', 'year': 1964}

# !!!^!!! UWAGA - komenda del thisdict wywali cały słownik w kosmos!

# jeśli chcemy wyczyścić słownik, używamy komendy clear():
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) # wyjście: {}   (tak, tylko nawias)

###&&&___^___&&&### LOOP DICTIONARIES
# loop through a dictionary
# all key names, one by one:
for x in thisdict:
  print(x)
  
# print all values in the dictionary:
for x in thisdict:
  print(thisdict[x])

# możliwe jest również wywołanie wartości czy kluczy komendami:
for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)
  
# pętla przez klucze i wartości jednocześnie, przy pomocy komendy items():
for x, y in thisdict.items():
  print(x, y)
  
###&&&___^___&&&### COPY DICTIONARIES - Nie możesz skopiować słownika po prostu wpisując dict2 = dict1, 
# ponieważ: dict2 będzie tylko odniesieniem do dict1, a zmiany dokonane w dict1 zostaną automatycznie wprowadzone również w dict2.
# jedną z dróg do skopiowania jest wbudowana komenda copy()

# Przykład:
kontynent = {
  "państwo": "Nilfgaard",
  "władca": "Emhyr var Emreis",
  "godło": "Słońce"
}

mydict = kontynent.copy()
print(mydict)
  
# Inną opcją na skopiowanie słownika jest funkcja dict():
kontynent = kontynent
mydict = dict(kontynent)
print(mydict)

###&&&___^___&&&### NESTED DICTIONARIES - słownik zawierający inne słowniki
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 

# Tworzenie słownika z trzech istniejących słowników:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 

# Access items in nested dictionaries - aby wyciągnąć dane z nested dictionary, musimy użyć nazw słowników zaczynając
# od zewnętrznego słownika. Przykład - wyświetlenie imienia dziecka nr 2:
print(myfamily["child2"]["name"]["year"]) # wyjście: Tobias

###&&&___^___&&&### DICTIONARY METHODS - python ma wbudowane funkcje dotyczące słowników:

kontynent.clear()       # Removes all the elements from the dictionary
kontynent.copy()        # Returns a copy of the dictionary
kontynent.fromkeys()    # Returns a dictionary with the specified keys and value
kontynent.get()         # Returns the value of the specified key
kontynent.items()       # Returns a list containing a tuple for each key value pair
kontynent.keys()        # Returns a list containing the dictionary's keys
kontynent.pop()         # Removes the element with the specified key
kontynent.popitem()     # Removes the last inserted key-value pair
kontynent.setdefault()  # Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
kontynent.update()      # Updates the dictionary with the specified key-value pai
kontynent.values()      # Returns a list of all the values in the dictionary


###&&&___#___&&&### PYTHON IF...ELSE
#python conditions and If statements
# if statement:
a = 33
b = 200
if b>a:
  print("b is greater than a")
  
# ELIF
a = 33
c = 33
if c > a:
  print("c is greater than a")
elif a == c:
  print("a and c are equal")
# ELSE - gdy już nic nie pasuje innego
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
### SHORT HAND IF: - można skrócić i napisać w tej samej linii. 
if a >b: print("a is greater than b")  
# podobnie z else:
a = 2
b = 330
print("A") if a > b else print("B")

# trzy warunki:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") 

#tak samo można działać z operatorem AND
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
# oraz OR:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# podobnie można potraktować operator NOT:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

### NESTER IF - nazywamy tak sytuację, gdy pod operatorem IF znajduje się inny operator IF:
x = 41
if x > 10:
  print("Above 10")
  if x > 20:
    print("also above 20")
  else:
    print("but not above 20")
    
# the pass statement:
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass

###&&&___#___&&&### python while loops - najprostsze pętle są wyrażone przez:
# while
# for

### the while loop - Za pomocą pętli while możemy wykonać zestaw instrukcji, o ile warunek jest spełniony.
# Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1
#Note: remember to increment i, or else the loop will continue forever.

#the break statement - można zatrzymać pętlę nawet jeśli spełnione są warunki:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
# the continue statement: continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i ==3:
    continue
  print(i)
  
# the else statement - With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  

###&&&___#___&&&### python FOR loops
# Pętla for służy do iteracji po sekwencji (czyli liście, krotce, słowniku, zestawie lub ciągu znaków).
# To mniej przypomina słowo kluczowe for w innych językach programowania i działa bardziej jak metoda iteratora, jaką można znaleźć w innych obiektowych językach programowania.
# Za pomocą pętli for możemy wykonać zestaw instrukcji, raz dla każdego elementu listy, krotki, zestawu itp.
# x - wszystkie. Coś jak * w SQL.

owoce = ["jagoda", "wiśnia", "banan"]
for x in owoce:
    print(x)
    
### looping through a string - pętla przez ciąg powoduje wyszczególnienie wszystkich znaków:
for x in "agrest":
    print(x)
    
### the break statement - przerwanie pętli dla określonego warunku.
# exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

warzywa = ["fasola", "ziemniak", "groch"]
for x in warzywa:
    print(x)
    if x == "ziemniak":
        break  # wyjście: fasola, ziemniak
    
### the continue statement - With the continue statement we can stop the current iteration of the loop, and continue with the next:
# do not print banana:
fruits = fruits
for x in fruits:
    if x == "banana":
        continue
    print(x) # wyjście: apple, cherry 
    
### THE RANGE FUNCTION - jeśli chcemy zrobić pętlę określoną liczbę razy używamy funkcji range():
for x in range(6):
    print(x)
#Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: 
# range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2,6):
    print(x) # wyjście- 2,3,4,5
    
# funkcja range domyślnie zwiększa parametr o 1, natomiast możliwe jest jego sprecyzowanie-
for x in range(2,30,3): #trzeci parametr to wielkość "skoku"
    print(x) # wyjście- 2,5,7,11 itd
    
print("==================")
    
### ELSE IN FOR LOOP - The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# przykład - wyświetlenie wartości przy użyciu pętli for loop od 0 do 5, a następnie poinformowanie o końcu:
for x in range(6):
    print(x)
else:
    print("koniec roboty, pętla skończona.")
# ważne - warunek "else" nie będzie wykonany, jeśli pętla zostanie wcześniej zatrzymana przez "break".
for x in range(6):
    if x == 3:
        break
    print(x) 
else:
    print("Zrobione") # wyjście - 0,1,2
    
### NESTED LOOPS - nested loop to pętla wewnątrz innej pętli:
# przykład - każdy przymiotnik dla każdego owocu:
adj = ["dorodny/a", "soczysty/a", "czerwony/a"]
owoc = ["pomidor", "wiśnia", "truskawka"]
for x in adj:
    for y in owoc:
        print(x,y)
        
### THE PASS STATEMENT - for loop nie może być puste, ale jeśli z jakiegoś powodu for loop nie ma wartości
# to wystarczy wstawić "pass" aby uniknąć wyświetlenia błędu:
for x in [0,1,2]:
    pass

###&&&___#___&&&### PYTHON FUNCTIONS
# funkcja to blok kodu, który jest uruchamiany jedynie, gdy zostanie wywołany.
# Do funkcji można przekazywać dane zwane parametrami. W rezultacie funkcja może zwrócić dane.

# tworzenie funkcji - tworzy się przez słowo kluczowe "def":
def my_function():
    print("Funkcyjne funkcjonalne siema")
    
# wywoływanie funkcji - aby wywołać funkcję, używamy jej nazwy:
my_function()

# dane/informacje mogą być przekazane do funkcji jako argumenty
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, 
# just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, 
# which is used inside the function to print the full name: 
  
def funkcja1(fname):
  print(fname + " Refsnes")
funkcja1("Emil")
funkcja1("Tobias")
funkcja1("Linus")
# Arguments are often shortened to args in Python documentations.

# parametry i argumenty z punktu widzenia funkcji:
# Parametr to zmienna wymieniona w nawiasach w definicji funkcji.
# Argument to wartość wysyłana do funkcji podczas jej wywoływania.

### number of arguments - By default, a function must be called with the correct number of arguments. 
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less. 

# funkcja oczekuje dwóch argumentów i dostaje dwa argumenty:
def funkcja2(fname, lname):
  print(fname + " " + lname)
  
funkcja2("Emiel", "Regis") # jeśli dalibyśmy jeden argument to wówczas otrzymamy błąd: TypeError: my_function() 
# missing 1 required positional argument: 'lname'

### ARBITRARY ARGUMENTS - *args - Arbitralne argumenty, *args
# Jeśli nie wiesz ile argumentów zostanie przekazanych do Twojej funkcji, dodaj * przed nazwą parametru w definicji funkcji.
# W ten sposób funkcja otrzyma krotkę argumentów i będzie mogła uzyskać dostęp do elementów:
# Przykład:

def funkcja3(*kids):
  print("The youngest child is " + kids[2]) # [2] - indeks argumentu
funkcja3("Emil", "Tobias", "Linus")

### KEYWORD ARGUMENTS - można dawać parametry/argumenty poprzez key = value
def funkcja3(child1, child2, child3):
  print("Moje dziecko to ")
funkcja3(child1 = "Ula", child2 = "Tymek", child3 = "Eliza")

### ARBITRARY KEYWORD ARGUMENTS = **kwargs 
# Jeżeli nie wiesz ile argumentów słów kluczowych zostanie przekazanych do Twojej funkcji, dodaj dwie gwiazdki: ** przed nazwą parametru 
# w definicji funkcji.
# W ten sposób funkcja otrzyma słownik argumentów i będzie mogła uzyskać dostęp do elementów:

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")   

### DEFAULT PARAMETER VALUE - poniższy przykład pokazuje użycie domyślnej wartości. 
# Działa to, gdy wywołamy funkcję nie podając jej argumentu:
def f_panstwo(country = "Norway"):
    print("I'm from " + country)
    
# Funkcja z argumentem:
f_panstwo("Argentina")
f_panstwo() # wyjście: I'm from Norway

### PASSING A LIST AS AN ARGUMENT - argumentem w funkcji może być praktycznie każdy typ danych:
# (string, number, list, dictionary etc.) i będzie to tak traktowane jak typ danych w definicji funkcji.
# np. argument typu lista pozostanie listą podczas wywoływania funkcji:
def f_jadlo(food):          # nazwa funkcji i jej X - czyli food.
    for x in food:          # to, co funkcja wykonuje - dla każdego elementu w X czyli food:
        print(x)            # wyświetl wynik
        
fruits = ["apple", "banana", "cherry"] # fruits=food, czyli nasze X funkcji.

f_jadlo(fruits)

### RETURN VALUE - aby funkcja zwróciła wartość musimy użyć komendy "return":

def mnozenie(x):
    return 5 * x
print(mnozenie(2))
print(mnozenie(5))
print(mnozenie(40))

### THE PASS STATEMENT - definicja funkcji nie może być pusta, ale jeśli istnieje powód, dla którego definicja
# ma być pusta, to korzystamy z "pass", jak w poprzednich przypadkach:
def funkcja_e():
    pass

### POSITIONAL-ONLY ARGUMENTS - możesz sprecyzować albo JEDYNIE argumenty pozycyjne albo JEDYNIE keyword arguments.
# aby sprecyzować funkcję do posiadania jedynie "positional arguments" dodaj " , / ":
def funkcja0(x, /):
    print(x)
funkcja0(3)    
# bez , / jest konieczność używania keyword arg nawet jeśli funkcja spodziewa się postinonal arg:
def funkcja1(x):
    print(x)
funkcja1(x = 3)  # błąd pokaże się, jeśli dodamy po argumencie , / a potem damy x = 3.

### KEYWORD-ONLY ARGUMENTS - aby sprecyzować, że funkcja może mieć tylko keyword args należy dodać *, przed argumentami
def funkcja2(*, x):
    print(x)
funkcja2(x = 3) # bez *, funkcja musi użyć positionale args nawet jeśli funkcja oczekuje kwargs.

### COMBINE POSITIONAL-ONLY and KEYWORD-ONLY - można zrobić kombinację dwóch typów argumentów w funkcji.
# wszystko PRZED / , to arg positional-only, natomiast wszystko po *, to keyword only.
def funkcja3(a, b, /, *, c, d):
    print(a + b + c + d)
funkcja3(5, 6, c=7, d=8)

### RECURSION
# Python akceptuje także rekursję funkcji, co oznacza, że zdefiniowana funkcja może wywołać samą siebie.
# Rekurencja jest powszechną koncepcją matematyczną i programistyczną. Oznacza to, że funkcja wywołuje samą siebie. 
# Ma to tę zaletę, że można przeglądać dane w pętli, aby osiągnąć wynik.
# Programista powinien zachować szczególną ostrożność w przypadku rekurencji, ponieważ dość łatwo może wpaść w napisanie funkcji, 
# która nigdy się nie kończy, lub takiej, która zużywa nadmierną ilość pamięci lub mocy procesora. 
# Jednakże, poprawnie napisana rekurencja może być bardzo wydajnym i matematycznie eleganckim podejściem do programowania.
# W tym przykładzie tri_recursion() jest funkcją, którą zdefiniowaliśmy tak, aby wywoływała samą siebie („recurse”). 
# Jako danych używamy zmiennej k, która zmniejsza się (-1) za każdym razem, gdy wykonujemy rekurencję. 
# Rekurencja kończy się, gdy warunek nie jest większy niż 0 (tj. gdy wynosi 0).
# Nowemu programiście sprawdzenie, jak to dokładnie działa, może zająć trochę czasu. 
# Najlepszym sposobem, aby się tego dowiedzieć, jest przetestowanie i modyfikacja

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
tri_recursion(6) # wyjście 1,3,6,10,15,21

###&&&___#___&&&### PYTHON LAMBDA - lambda to mała, utajniona funkcja.
# Wyrażenia lambda wykorzystuje się w miejscach, gdzie wymagany jest obiekt funkcyjny, ale pisanie w tym celu klasycznej funkcji 
# (z pomocą słowa kluczowego def) byłoby nieopłacalne.


# funkcja jednoparametrowa:
pole_kwadratu = lambda x: x*x
a = pole_kwadratu(6)

# funkcja bezparametrowa:
import datetime
aktualna_godzina = lambda datetime: datetime.now().hour
print(aktualna_godzina)

# funkcja dwuparametrowa
suma = lambda a, b: a+b
print(suma(4, 1))

x = lambda x, y: x*y
print(x(7, 3))

suma2 = lambda a, b, c: a + b - c
print(suma2(14, 3, 10))

# zastosowanie: stworzenie funkcji, która zawsze potraja zadaną wartość:
def myfunc(n):
    return lambda a: a * n
mytripler = myfunc(3)

print(mytripler(10))

# możliwe jest również użycia jednej lambdy w kilku funkcjach:

def mnozenie(n):
    return lambda a: a*n
mydoubler = mnozenie(2)
mytripler = mnozenie(3)

print(mydoubler(7))
print(mytripler(4))


######################################33

###&&&___^___&&&### Python Datetime
# Daty nie są domyślnym typem danych Pythona, więc musimy zaimportować moduł "datetime" aby pracować z datami.

import datetime

x = datetime.datetime.now()
print(x)

### Date Output
# wynikiem wcześniejszej operacji będzie aktualna data i czas. Istnieje wiele możliwości wyświetlania danych.

# return the year and name of weekday:
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

### Creating Date Objects
# aby stworzyć datę, możemy użyć klasy datetime() z modułu datetime.
# klasa datetime wymaga trzech parametrów do stworzenia daty: roku, miesiąca i dnia.

# stworzenie obiektu/daty

import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

# klasa datetime() także posiada parametry czasu i strefy czasowej, lecz są one opcjonalne. 
# Ich domyślna wartość wynosi 0.

### The strftime() Method
# obiekt datetime posiada metodę, która formatuje daty na ciągi python.
# Ta metoda to strftime() i posiada ona jeden parametr - format. Określa on format zwracanaego ciągu.
# przykład: wyświetl nazwę miesiąca

import datetime

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

# Inny przykład: parametr format "%C" wskazuje wiek, lecz nie działa on prawidłowo.

import datetime

x = datetime.datetime(1995, 6, 1)
print(x.strftime("%C")) # wyjście: 19. No nie - to XX wiek.

# Aby to poprawić:
x = datetime.datetime(1995, 6, 1) 
y = x.strftime("%C")  # mamy str na wyjściu i nieszczęsny "19" wiek
z = int(y) + 1 # zmieniamy str na int i dodajemy brakującą jedynkę
print(z) # wyjście: 20 - prawidłowo.


###&&&___^___&&&### Python PIP
# PIP to menedżer modułów pythonowych. W wersjach Pythona 3.4 i wyższych, PIP jest domyślnie wbydowany.

### What is package?
# package - nazwijmy to paczką - zawiera wszystkie pliki potrzebne dla modułu.
# Moduły w Pythonie to biblioteki kodu, które mogą być zaimplementowane w naszych projektach.

# Sprawdzenie zainstalowania i wersji PIP:
# W wierszu poleceń: pip --version

# Instalacja pip - znajdź w google/wejdź na stronę pypi.org/project/pip/

### Pobieranie paczek
# Aby pobrać paczkę, należy w cmd wpisać komendę zawierającą nazwę paczki:

# pip install camelcase

# Po zatwierdzeniu paczka camelcase się pobierze i zainstaluje.

### Używanie paczek/modułów
# aby użyć modułu w skrypcie, należy go zaimportować:
import camelcase

c = camelcase.CamelCase()
txt = "jakaś treść"
print(c.hump(txt))

### Wyszukiwanie modułów 
# moduły można wyszukać na stronie pypi.org

### Usuwanie paczek
# aby usunąć daną paczkę, korzystamy z komendy uninstall w cmd:

# pip uninstall camelcase

# wiersz poleceń będzie potrzebował zatwierdzenia i gotowe.

### Lista paczek/modułów
# aby wyświetlić listę modułów, w cmd wpisujemy:

# pip list

###&&&___^___&&&### Python String Formatting - formatowanie przeprowadzamy, aby mieć pewność, że otrzymamy to co chcemy komendą print().
# Komenda format() umożliwia zmianę wskazanych elementów ciągu. Aby tego dokonać korzystamy z nawiasów {}

# Przykład: dodanie ceny
price = 49
txt = "The price is {} euro"
print(txt.format(price))

# Przykład - wyświetlanie wartości z dwoma miejscami po przecinku.
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Wszystkie metody formatowania znajdują się tutaj: https://www.w3schools.com/python/ref_string_format.asp

### Multiple Values
# Jeśli chcemy zmienić kilka wartości, to musimy je dodać w komendzie format():
print(txt.format(price, itemno, count))

#oraz dodać nawiasy {} aby umiejscowić te wartości:

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} euro"
print(myorder.format(quantity, itemno, price))

### Index Numbers - można użyć indeksów w nawiasach {} aby być pewnym, że umiejscowimy wartości w odpowiednich miejscach:
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} euro."

# Można też dodawać jedną wartość w większej ilości miejsc:
age = 36
name = "John"

###&&&___^___&&&### Python User Input
# Python umożliwia ręczne wprowadzanie wartości. W wersji Python od 3.6 w górę jest to komenda input()
# Przykład - wprowadzenie nazwy użytkownika, która będzie wyświetlona na ekranie:

username = input("Enter username:")
print("Username is: " + username)

# Python stops executing when it comes to the input() function, and continues when the user has given some input.

###&&&___^___&&&### Python Math
# Python posiada wbudowane funkcje dotyczące operacji matematycznych.
# Przykład - funkcje min() i max():
x = min(5, 10, 15)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25) # wartość bezwzględna, wyjście 7.25
print(x)

# pow(x, y) to nic innego, jak potęgowanie.
x = pow(4, 3) # 4 do potęgi 3
print(x)

### The Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions.
# To use it, you must import the math module:

import math

# When you have imported the math module, you can start using methods and constants of the module.
# The math.sqrt() method for example, returns the square root of a number:

x = math.sqrt(64) # pierwiastek kwadratowy z 64
print(x)  # wyjście = 8

# The math.ceil() method rounds a number upwards to its nearest integer, and 
# the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1 

# The math.pi constant, returns the value of PI (3.14..
x = math.pi
print(x)

###&&&___^___&&&### Python Modules
# Moduł można rozpatrywać jako bibliotekę kodu. Moduł zawiera zestaw funkcji,
# które chcemy zawrzeć w naszym kodzie/aplikacji.

### Create a Module
# aby stworzyć moduł, musimy zapisać kod w pliku z rozszerzeniem .py

def greeting(name, land):
    print("Hello," + name + " from " + land) #zapisano jako mymodule.py
    
### Use a Module
# aby wykorzystać moduł w kodzie, musimuy go zaimportować:

import mymodule

mymodule.greeting("Geralt", "Rivia")

# Note: When using a function from a module, use the syntax: module_name.function_name.

### Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
# Umieśćmy poniższy kod w mymodule.py:

person1 = {
        "name": "Cahir",
        "age": 36,
        "land": "Nilfgaard"
    }

# Import modułu i dostęp do wpisu person1:

import mymodule

a = mymodule.person1["age"]
print(a)

### nazwy modułów - dowolne. Ważne, że z rozszerzeniem .py

### Built-in Modules
# istnieje kilka modułów wbudowanych w Pythona. Przykład:

import platform

x = platform.system()
print(x)  # wyjście: Windows

### Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

# Przykład: stwórz listę nazw należących do modułu "platform".

import platform
x = dir(platform)
print(x)

### Import from Module
# Możliwy jest wybór tego, którą część moduły zaimportujemy, z użyciem "from":

from mymodule import person1
print(person1["age"])

# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]

###&&&___^___&&&### Python Try Except
try # pozwala przetestować blok kodu pod kątem błędów
except # pozwala obsłużyć błąd.
else # umożliwia wykonanie kodu, gdy nie ma błędu.
finally # umożliwia wykonanie kodu, niezależnie od wyniku bloków try- i require.

### Exception Handling
# Gdy wystąpi błąd lub wyjątek, jak go nazywamy, Python zwykle zatrzyma się i wygeneruje komunikat o błędzie.
# Te wyjątki można obsłużyć za pomocą instrukcji try:

# Przykład: The try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print("Wystąpił wyjątek")
# Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error:
# This statement will raise an error, because x is not defined:

### Many Exceptions
# Możesz zdefiniować dowolną liczbę bloków wyjątków, np.: jeśli chcesz wykonać specjalny blok kodu dla specjalnego rodzaju błędu:
# Przykład: Print one message if the try block raises a NameError and another for other errors:

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something is still not yes")

### Else  
# Możesz użyć słowa kluczowego else, aby zdefiniować blok kodu, który zostanie wykonany, jeśli nie zostaną zgłoszone żadne błędy:
# n this example, the try block does not generate any error:

try:
  print("Hello")
except:
  print("Something went wrong bro")
else:
  print("Wszystko gitówa")

### Finally
# Blok "finally", jeśli został określony, zostanie wykonany niezależnie od tego, czy blok "try" zgłosi błąd, czy nie.
try:
  print(x)
except:
  print("Something went wrong bro")
finally:
  print("Skrypt zakończony")
  
# This can be useful to close objects and clean up resources:
try:
  f = open("file.txt")
  try:
    f.write("Cimcirimci")
  except:
    print("Coś nie ten teges z tym plikiem")
  finally:
    f.close()
except:
  print("Coś nie poszło mordo") # The program can continue, without leaving the file object open.
  
### Raise an exception 
# Jako programista Pythona możesz zgłosić wyjątek, jeśli wystąpi warunek. Aby zgłosić (lub zgłosić) wyjątek, użyj słowa kluczowego raise.
# Przykład: raise an error and stop the program if x is lower than 0:

x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero bro")

# The raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.
# Raise a TypeError if x is not an integer:

x = "mordo"
if not type(x) is int:
  raise TypeError("Tylko numery, mordo")

###&&&___^___&&&### Python Iterators
# Iterator – obiekt pozwalający na sekwencyjny dostęp do wszystkich elementów lub części zawartych w innym obiekcie, zwykle kontenerze lub liście. 
# Iterator jest czasem nazywany kursorem, zwłaszcza w zastosowaniach związanych z bazami danych. 

# Iterator to obiekt zawierający policzalną liczbę wartości.
# Iterator to obiekt, po którym można iterować, co oznacza, że można przechodzić przez wszystkie wartości.
# Technicznie rzecz biorąc, w Pythonie iterator to obiekt implementujący protokół iteratora, na który składają się metody __iter__() i __next__().

### Iterator vs Iterable
# Listy, krotki, słowniki i zbiory są obiektami iterowalnymi. Są to iterowalne kontenery, z których można uzyskać iterator.
# Wszystkie te obiekty mają metodę iter(), która służy do uzyskania iteratora:

# Przykład:
# return an iterator from a tuple and print each value:
mytuple = (12, 72, 26, 8)
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Także strings (szyki) są obiektami iterowalnymi:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit)) # ..... itd

### Looping Through an Iterator
# Możemy użyć pętli for aby iterować obiekty iterowalne:
mytuple = (12, 26, 8, 72)

for x in mytuple:
    print(x)
    
# tak samo w przypadku string:
mystr = "hakuna matata"
for x in mystr:
    print(x)
    
# Pętla for w rzeczywistości tworzy obiekt iteratora i wykonuje metodę next() dla każdej pętli.

### Create an Iterator
# Aby utworzyć obiekt/klasę jako iterator, musisz zaimplementować metody __iter__() i __next__() w swoim obiekcie.
# Tak jak można było się nauczyć w rozdziale classes/objects, wszystkie klasy posiadają funkcję zwaną __init__(),
# która umożliwia zainicjiowanie akcji, gdy obiekt zostaje utworzony.
# Komenda __iter__() działa podobnie, możesz wykonywać operacje (inicjowanie itp.), ale zawsze musisz zwrócić sam obiekt iteratora.
# Metoda __next__() umożliwia również wykonywanie operacji i musi zwracać następny element w sekwencji.

# Przykład: 
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter)) 

### Stop Iteration
# Powyższy przykład nie miałby końca, ponieważ zawsze istniałby warunek __next__().
# Aby nie doszło do  sytuacji wiecznego iterowania, musimy wykorzystać komendę StopIteration.
# W metodzie __next__() możemy dodać warunek kończący, aby zgłosić błąd, jeśli iteracja zostanie wykonana określoną liczbę razy:

# Przykład: zakończ iterację po 20 powtórzeniach:
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a 
            self.a += 1
            return x
        else: 
            raise StopIteration
        
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)



###&&&___^___&&&### Polymorphism
# Słowo „polimorfizm” oznacza „wiele form”, a w programowaniu odnosi się do metod/funkcji/operatorów o tej samej nazwie, które można wykonać na wielu obiektach lub klasach.

# Przykład: funkcja len() w string - ilość znaków:
x = "Dolina rzeki Pontar"
print(len(x))

# funkcja len() w krotce - ilość elementów:
mytuple = ("apple", "banana", "cherry")
print(len(mytuple)) 

# For dictionaries len() returns the number of key/value pairs in the dictionary:
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict)) # wyjście: 3

### Class Polymorphism
# Polimorfizm jest często używany w metodach klasowych, gdzie możemy mieć wiele klas o tej samej nazwie metody.
# Załóżmy na przykład, że mamy trzy klasy: Car, Boat i Plane i wszystkie mają metodę zwaną move():

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Drive!")
        
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Sail!")
        
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang") # create a car class
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()
# wyjście: Drive! Sail! Fly! 

# Spójrz na pętlę for na końcu. Ze względu na polimorfizm możemy wykonać tę samą metodę dla wszystkich trzech klas.

### Inheritance Class Polymorphism (inheritance - dziedzictwo)
# A co z zajęciami z klasami podrzędnymi o tej samej nazwie? Czy możemy tam zastosować polimorfizm?
# Tak. Jeśli skorzystamy z powyższego przykładu i utworzymy klasę nadrzędną o nazwie Vehicle 
# oraz utworzymy klasy podrzędne Car, Boat, Plane z Vehicle, klasy podrzędne dziedziczą metody Vehicle, ale mogą je zastąpić:

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Move!")
    
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")  
        
class Plane(Vehicle):
  def move(self):
    print("Fly!")         

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

# wyjście: Ford
# Mustang
# Move!
# Ibiza
# Touring 20
# Sail!
# Boeing
# 747
# Fly!

# Klasy podrzędne dziedziczą właściwości i metody z klasy nadrzędnej.
# W powyższym przykładzie widać, że klasa Car jest pusta, ale dziedziczy markę, model i funkcję move() z Vehicle.
# Klasy Boat i Plane również dziedziczą markę, model i metodę move() z Vehicle, ale obie zastępują metodę move().
# Ze względu na polimorfizm możemy wykonać tę samą metodę dla wszystkich klas.


###&&&___^___&&&### Python Scope (zakres)
# Zmienna jest dostępna tylko w regionie, w którym została utworzona. Nazywa się to zakresem.

### Local Scope A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# Przykład: zmienna stworzona wewnątrz funkcji jest osiągalna tylko w niej:

def myfunc():
    x = 300
    print(x)
    
myfunc()

### Function inside function
# Jak wyjaśniono w powyższym przykładzie, zmienna x nie jest dostępna poza funkcją, ale jest dostępna dla dowolnej funkcji wewnątrz funkcji:
    
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
    
myfunc()

### Global Scope
# Zmienna utworzona w głównej części kodu Pythona jest zmienną globalną i należy do zasięgu globalnego.
# Zmienne globalne są dostępne w dowolnym zakresie, globalnym i lokalnym.

x = 300

def myfunc():
    print(x)
    
myfunc()

print(x)

### Naming Variables
# Jeśli operujesz tą samą nazwą zmiennej wewnątrz i na zewnątrz funkcji, Python potraktuje je jako dwie osobne zmienne, 
# jedną dostępną w zasięgu globalnym (poza funkcją) i drugą dostępną w zasięgu lokalnym (wewnątrz funkcji):

# Przykład: The function will print the local x, and then the code will print the global x:

x = 300

def myfunc():
    x = 200
    print(x)
    
myfunc() # 200

print(x) # 300

### Global Keyword
# Jeśli chcesz utworzyć zmienną globalną, ale utkniesz w zasięgu lokalnym, możesz użyć słowa kluczowego global.
# Słowo kluczowe global sprawia, że zmienna jest globalna.

def myfunc():
    global x
    x = 300
    
myfunc()
print(x)

# Użyj także słowa kluczowego global, jeśli chcesz dokonać zmiany w zmiennej globalnej wewnątrz funkcji.
x = 300

def myfunc():
    global x
    x = 200
    
myfunc()
print(x)

###&&&___^___&&&### Python JSON
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# Python posiada wbudowaną paczkę json która może być stosowana do pracy z danymi JSON.

import json

### Parse JSON - Convert from JSON to Python
# Jeśli masz ciąg JSON, możesz go przeanalizować za pomocą metody json.loads().
# Rezultatem będzie słownik Pythona.

# Przykład:

import json
# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# konwersja do JSON:
y = json.dumps(x)

# rezultat - ciąg JSON
print(y)

# You can convert Python objects of the following types, into JSON strings:
# dict, list, tuple, string, int, float, true, false, none
    
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Inny przykład: konwersja obiektu Python, który posiada różne typy danych:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

### Format the result - Sformatuj wynik
# Powyższy przykład drukuje ciąg JSON, ale nie jest on zbyt łatwy do odczytania, bez wcięć i podziałów wierszy.
# Metoda json.dumps() posiada parametry ułatwiające odczytanie wyniku:

# Use the indent parameter to define the numbers of indents:
json.dumps(x, indent=4)

# wyjście:
{
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
} 

# Możesz także zdefiniować separatory, wartość domyślna to (", ", ": "), co oznacza użycie przecinka i spacji 
# do oddzielenia poszczególnych obiektów oraz dwukropka i spacji do oddzielenia kluczy od wartości:
# Use the separators parameter to change the default separator:
json.dumps(x, indent=4, separators=(". ", " = "))

### Order the result:
# Metoda json.dumps() posiada parametry umożliwiające uporządkowanie kluczy w wyniku:
# Użyj parametru sort_keys, aby określić, czy wynik powinien być posortowany, czy nie

json.dumps(x, indent=4, sort_keys=True)





#=======================================================================================

###&&&___^___&&&### Python Classes and Objects

# Python jest obiektowym językiem programowania. Praktycznie wszystko w Pythonie jest obiektem,
# wraz ze swoimi właściwościami i metodami.
# Class to taki konstruktor obiektów albo "projekt" do tworzenia obiektów.

# Aby stworzyć klasę wykorzystujemy keyword "class":
class MyClass:
    x = 5
    
### Create Object
# Teraz możemy użyć utworzonej klasy do stworzenia obiektów.
# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)

### The __init___() Function

# powyższe przykłady były proste i nie obrazują zupełnie funkcji klasy.
# Aby w pełni to zrozumieć, musimy pojąć znaczenie funkcji __init__()
# Wszystkie klasy mają funkcję __init__(), która zawsze jest wykonywana podczas inicjowania klasy.
# Używamy funkcji __init__() do przyporządkowania wartości do właściwości obiektu lub do innych akcji
# które trzeba wykonać, gdy obiekt zostaje stworzony.

# Utwórz klasę o nazwie Person i użyj funkcji __init__(), aby przypisać wartości do imienia i wieku:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Uwaga: Funkcja __init__() jest wywoływana automatycznie za każdym razem, gdy klasa jest używana do tworzenia nowego obiektu.

### The __str__() Function
# Funkcja __str__() kontroluje, co powinno zostać zwrócone, gdy obiekt klasy jest reprezentowany jako ciąg znaków.
# Jeśli funkcja __str__() nie jest ustawiona, zwracana jest ciąg znaków reprezentujący obiekt:

# przedstawienie ciągu obiektu bez funkcji __str__():
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
p1 = Person("John", 36)
print(p1)   #wyjście <__main__.Person object at 0x15039e602100> 

# przedstawienie ciągu obiektu z funkcją __str__():
class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age
      
    def __str__(self):
      return f"{self.name}({self.age})"
    
p1 = Person("John", 36)
print(p1) #wyjście John(36)

### Object Methods
# Obiekty mogą również zawierać metody. Metody w obiektach to funkcje należące do obiektu.
# Stwórzmy metodę w klasie Person:

# Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def myfunc(self):
    print("Hello my name is " + self.name)
    
p1 = Person("John", 36)
p1.myfunc()

# Uwaga: Parametr self jest odniesieniem do bieżącej instancji klasy i służy do uzyskiwania dostępu do zmiennych należących do klasy.

### The self Parameter
# Parametr self jest odniesieniem do bieżącej instancji klasy i służy do uzyskiwania dostępu do zmiennych należących do klasy.
# Nie musi mieć nazwy self , możesz ją nazwać jak chcesz, ale musi to być pierwszy parametr dowolnej funkcji w klasie:

# Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age
    
  def myfunc(abc):
    print("Hello my name is " + abc.name)
    
  p1 = Person("John", 36)
  p1.myfunc()
  
### Modify Object Properties - można usuwać właściwości obiektu przy użyciu del:

del p1.age

### Delete Objects - także przy użyciu komendy del:

del p1

### The pass Statement: definicja klasy nie może być pusta, nie mniej, jeśli potrzeba jest taką stworzyć, to można użyć komendy pass, aby 
# nie wyświetlało błędu przy tworzeniu:

class Person:
  pass




#___________________________________________________^^^^^^^^^^^^^^^^^^^^^^^^_____________________________________

###&&&___^___&&&### Python File Handling
# Obsługa plików to element każdej aplikacji. Python posiada kilka funkcji dla tworzenia, edycji, odczytu i usuwania plików.

# Funkcja Pythona do pracy nad plikami to open(). Ta funkcja posiada dwa parametry: nazwa pliku i tryb (filename/mode)
# Tryby:

"r" # Read - Default value. Opens a file for reading, error if the file does not exist
"a" # Append - Opens a file for appending, creates the file if it does not exist (append - dodać)
"w" # Write - Opens a file for writing, creates the file if it does not exist
"x" # Create - Creates the specified file, returns an error if the file exists

# dodatkowo są dwa tryby: tekstowt i binarny (jeśli tak chcemy je edytować)
"t" # Text - Default value. Text mode
"b" # Binary - Binary mode (e.g. images)

### Syntax
# open file for reading
f = open("demofile.txt")

# Kod powyżej to to samo co:
f = open("demofile.txt", "rt")

# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

###&&&___^___&&&### Python File Open (w katalogu src)
f = open("src/tekst.txt", "r")
print(f.read())

# lub tak:
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read()) 

### Read Only Parts of the File
# Domyślnie komenda read() zwraca cały tekst. Jeśli chcemy sprecyzować, ile znaków mamy otrzymać, to dopisujemy to parametrem w f.read()
f = open("demofile.txt", "r")
print(f.read(5))

### Read Lines
# You can return one line by using the readline() method:
f = open("demofile.txt", "r")
print(f.readline()) 

# By calling readline() two times, you can read the two first lines:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline()) 

# przepuszczając pętlę przez skrypt otrzymamy cały tekst, linijka po linijce:
f = open("demofile.txt", "r")
for x in f:
  print(x)

### Close Files
# It is a good practice to always close the file when you are done with it.
f = open("demofile.txt", "r")
print(f.readline())
f.close()

# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

###&&&___^___&&&### Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# Przykład:

f = open("demofile.txt", "a")
f.write("Now the file has more content")
f.close()

# open and read the file agter the appending:
f = open("demofile.txt", "r")
print(f.read())

# Overwrite the content:
f = open("demofile.txt", "w")
f.write("Ups, nadpisałem!")
f.close()

# otwórz i odczytaj:
f = open("demofile.txt", "r")
print(f.read())

# Note: the "w" method will overwrite the entire file.
# To create a new file in Python, use the open() method, with one of the following parameters:
#   "x" - Create - will create a file, returns an error if the file exist
#   "a" - Append - will create a file if the specified file does not exist
#   "w" - Write - will create a file if the specified file does not exist

f = open("myfile.txt", "x")

###&&&___^___&&&### Python Delete File
# Aby usunąć plik, musisz zaimportować moduł OS i odpalić jedną z jego funkcji: os.remove()

# Przykład:
import os
os.remove("demofile.txt")

# Check, if file exists:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("Plik nie istnieje")
  
### Delete folder
# Aby usunąć cały folder, użyj komendy os.rmdir():
import os
os.rmdir("myfolder")
# Note: You can only remove empty folders.

