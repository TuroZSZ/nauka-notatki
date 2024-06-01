###&&&___^___&&&### Data Science - Data Preparation

# Przed analizą danych analityk danych musi je wyodrębnić, uczynić je czystymi i wartościowymi.
# Zanim dane będą mogły być analizowane, należy je zaimportować/wyodrębnić.
# W poniższym przykładzie pokazujemy, jak importować dane za pomocą Pandas w Pythonie.
# Używamy funkcji read_csv() do importowania pliku CSV z prawidłowymi:

import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")

print(health_data)

# Wyjaśnienie powyższego przykładu:

#     Zaimportuj bibliotekę Pandas
#     Nadaj ramce danych nazwę health_data.
#     header=0 oznacza, że nagłówki nazw zmiennych znajdują się w pierwszym wierszu (pamiętaj, że 0 oznacza pierwszy wiersz w Pythonie)
#     sep="," oznacza, że "," jest używane jako separator pomiędzy wartościami. Dzieje się tak, ponieważ używamy typu pliku .csv (wartości rozdzielane przecinkami)

# Wskazówka: jeśli masz duży plik CSV, możesz użyć funkcji head(), aby wyświetlić tylko 5 górnych wierszy

print(health_data.head())

# Dane: 
# https://www.w3schools.com/datascience/ds_analyze_data.asp?goalId=05101efd-45ce-4746-805d-5b9a8b327a59

### Data Cleaning
# Spójrz na zaimportowane dane. Jak widać, dane są „brudne” i zawierają błędnie lub niezarejestrowane wartości:

# Problemy:
#     Jest kilka pustych pól
#     Średni puls 9 000 nie jest możliwy
#     Liczba 9 000 będzie traktowana jako liczba nieliczbowa ze względu na separator spacji
#     Jedna obserwacja maksymalnego tętna jest oznaczona jako „AF”, co nie ma sensu

# Musimy więc wyczyścić dane, aby przeprowadzić analizę.

# Widzimy, że wartości nienumeryczne (9 000 i AF) znajdują się w tych samych wierszach i zawierają brakujące wartości.
# Rozwiązanie: Aby rozwiązać ten problem, możemy usunąć wiersze z brakującymi obserwacjami.
# Kiedy ładujemy zestaw danych za pomocą Pand, wszystkie puste komórki są automatycznie konwertowane na wartości „NaN”.
# Zatem usunięcie komórek NaN daje nam czysty zestaw danych, który można przeanalizować.
# Możemy użyć funkcji dropna() do usunięcia NaN. oś=0 oznacza, że chcemy usunąć wszystkie wiersze posiadające wartość NaN:

health_data.dropna(axis=0, inplace=True)
print(health_data)

### Data Categories

# Aby analizować dane, musimy także wiedzieć, z jakimi rodzajami danych mamy do czynienia.

# Dane można podzielić na trzy główne kategorie:

#     Numeryczne — zawiera wartości liczbowe. Można podzielić na dwie kategorie:
#         Dyskretny: Liczby są liczone jako „całe”. Przykład: Nie możesz przeszkolić 2,5 sesji, są to 2 lub 3
#         Ciągły: Liczby mogą mieć nieskończoną precyzję. Na przykład możesz spać 7 godzin, 30 minut i 20 sekund, czyli 7,533 godzin
#     Kategoryczne – zawiera wartości, których nie można ze sobą porównać. Przykład: kolor lub rodzaj treningu
#     Porządkowe — zawiera dane kategoryczne, które można ze sobą porównać. Przykład: Oceny w szkole, gdzie A jest lepsze niż B i tak dalej

# Znając typ swoich danych, będziesz wiedział, jaką technikę zastosować podczas ich analizy.

### Data Types

# Możemy użyć funkcji info() aby określić typ danych:

print(health_data.info())

# Widzimy, że ten zbiór danych zawiera dwa różne typy danych:

#     Float64
#     Obiekt

# Nie możemy tutaj używać obiektów do obliczeń i przeprowadzania analiz. Musimy przekonwertować obiekt typu na float64 (float64 to liczba z ułamkiem dziesiętnym w Pythonie).
# Możemy użyć funkcji astype() do konwersji danych na float64.
# Poniższy przykład konwertuje „Average_Pulse” i „Max_Pulse” na typ danych float64 (pozostałe zmienne mają już typ danych float64):

health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)

print (health_data.info()) 

### Analyze the Data

# Po oczyszczeniu zbioru danych możemy przystąpić do analizy danych.
# Do podsumowania danych możemy użyć funkcji describe() w Pythonie:

print(health_data.describe()) 

# wynik:
    # Count — zlicza liczbę obserwacji
    # Mean — wartość średnia
    # Std — odchylenie standardowe (wyjaśnione w rozdziale poświęconym statystyce)
    # Min – najniższa wartość
    # 25%, 50% i 75% to percentyle (wyjaśnione w rozdziale poświęconym statystykom)
    # Max - Najwyższa wartość

###&&&___^___&&&### Data Science - Linear Functions

# Funkcje liniowe. Wałkowałem to tyle razy, że notatek nie trzeba.

###&&&___^___&&&### Data Science - Plotting Linear Functions

# Plot the Existing Data in Python
# Now, we can first plot the values of Average_Pulse against Calorie_Burnage using the matplotlib library.
# The plot() function is used to make a 2D hexagonal binning plot of points x,y:

import matplotlib.pyplot as plt

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line'),
plt.ylim(ymin=0)
plt.xlim(xmin=0)

plt.show() 

#     Zaimportuj moduł pyplot z biblioteki matplotlib
#     Wykreśl dane z Average_Pulse względem Calorie_Burnage
#     kind='line' mówi nam, jaki typ fabuły chcemy. Tutaj chcemy mieć linię prostą
#     plt.ylim() i plt.xlim() mówią nam, od jakiej wartości chcemy, aby rozpoczynała się oś. Tutaj chcemy, aby oś zaczynała się od zera
#     plt.show() pokazuje nam wynik

# Powyższy kod zwróci następujący wynik:

###&&&___^___&&&### Data Science - Slope and Intercept

# Nachylenie i przecięcie

# Teraz wyjaśnimy, jak obliczyliśmy nachylenie i punkt wyrazu naszej funkcji:
# f(x) = 2x + 80

# Poniższy obrazek wskazuje na nachylenie – które wskazuje, jak stroma jest linia, oraz punkt przecięcia – będący wartością y, gdy x = 0 (punkt, w którym linia ukośna przecina oś pionową). 
# Czerwona linia jest kontynuacją niebieskiej linii z poprzedniej strony.

### Find Slope:

# Nachylenie definiuje się jako o ile wzrasta spalanie kalorii, jeśli średni puls wzrasta o jeden. Mówi nam, jak „stroma” jest linia ukośna.
# Nachylenie możemy znaleźć, korzystając z proporcjonalnej różnicy dwóch punktów z wykresu.

#     Jeśli średni puls wynosi 80, spalanie kalorii wynosi 240
#     Jeśli średni puls wynosi 90, spalanie kalorii wynosi 260

# Widzimy, że jeśli średni puls wzrośnie o 10, spalanie kalorii wzrośnie o 20.

# Slope = 20/10 = 2

# The slope is 2.
# Mathematically, Slope is Defined as:
# Slope = f(x2) - f(x1) / x2-x1

# f(x2) = Second observation of Calorie_Burnage = 260
# f(x1) = First observation of Calorie_Burnage = 240
# x2 = Second observation of Average_Pulse = 90
# x1 = First observation of Average_Pulse = 80
# Slope = (260-240) / (90 - 80) = 2

# Sprawdzenie nachylenia z wykorzystaniem Pythona:

def slope(x1, y1, x2, y2):
    s = (y2-y1)/(x2-x1)
    return s

print(slope(80,240,90,260)) # wyjście: 2.0

### Znajdź przechwyt

# Przecięcie służy do dostrojenia funkcji przewidywania spalenia kalorii.
# Punkt przecięcia to miejsce, w którym ukośna linia przecina oś y, jeśli została całkowicie narysowana.
# Przecięcie jest wartością y, gdy x = 0.
# Widzimy tutaj, że jeśli średni puls (x) wynosi zero, wówczas spalanie kalorii (y) wynosi 80.

# Zatem punkt przecięcia wynosi 80.
# Czasami przechwytywanie ma znaczenie praktyczne. Czasami nie.

# Czy ma sens, że średni puls wynosi zero?
# Nie, byłbyś martwy i na pewno nie spaliłbyś żadnych kalorii.

# Musimy jednak uwzględnić wyraz wolny, aby uzupełnić zdolność funkcji matematycznej do prawidłowego przewidywania spalenia kalorii.

# Inne przykłady, w których wyraz wolny funkcji matematycznej może mieć praktyczne znaczenie:
#     Przewidywanie przychodów w przyszłym roku na podstawie wydatków na marketing (Jakie przychody będziemy mieli w przyszłym roku, jeśli wydatki na marketing wyniosą zero?). Można założyć, że firma nadal będzie osiągać pewne przychody, nawet jeśli nie wyda pieniędzy na marketing.
#     Zużycie paliwa w zależności od prędkości (Ile paliwa zużywamy, jeśli prędkość wynosi 0 mil na godzinę?). Samochód zasilany benzyną będzie nadal zużywał paliwo na biegu jałowym.

### Find the Slope and Intercept Using Python

# Funkcja np.polyfit() zwróci nam nachylenie i miejsce przecięcia:

import pandas as pd
import numpy as np

health_data = pd.read_csv("data.csv", header=0, sep=",")

x = health_data["Średni puls"]
y = health_data["Spalanie kalorii"]

slope_intercept = np.polyfit(x,y,1)

print(slope_intercept) # wyjście: [ 2. 80.] 

# Wyjaśnienie przykładu:

#     Wyodrębnij zmienne Average_Pulse (x) i Calorie_Burnage (y) z health_data.
#     Wywołaj funkcję np.polyfit().
#     Ostatni parametr funkcji określa stopień funkcji, który w tym przypadku wynosi „1”.

# Wskazówka: funkcje liniowe = funkcja 1 stopnia. W naszym przykładzie funkcja jest liniowa i mieści się w zakresie 1 stopnia. 
# Oznacza to, że wszystkie współczynniki (liczby) są potęgi jeden. Obliczyliśmy teraz nachylenie (2) i wyraz wolny (80). Funkcję matematyczną możemy zapisać w następujący sposób:
# Przewiduj spalanie kalorii, używając wyrażenia matematycznego:
# f(x) = 2x + 80
# Zadanie:
# Teraz chcemy przewidzieć spalanie kalorii, jeśli średni puls wynosi 135.
# Pamiętaj, że wyraz wolny jest stałą. Stała to liczba, która się nie zmienia.

# Możemy teraz zastąpić dane wejściowe x liczbą 135:
# f(135) = 2 * 135 + 80 = 350
# Jeśli średni puls wynosi 135, spalanie kalorii wynosi 350.

# Define the Mathematical Function in Python
# Here is the exact same mathematical function, but in Python. The function returns 2*x + 80, with x as the input:

def my_function(x):
    return 2*x + 80

print(my_function(135))

### Plot a New Graph in Python

# Here, we plot the same graph as earlier, but formatted the axis a little bit.
# Max value of the y-axis is now 400 and for x-axis is 150:

import matplotlib.pyplot as plt

health_data.plot(x = "średni puls", y = "spalanie kalorii", kind = 'line'),
plt.ylim(ymin = 0, ymax = 400)
plt.xlim(xmin = 0, xmax = 150)

plt.show()

###&&&___^___&&&### Data Science - Intro to Statistics

# Statystyka to nauka zajmująca się analizą danych.
# Kiedy stworzymy model przewidywania, musimy ocenić wiarygodność przewidywania. Bo cóż warta jest przepowiednia, jeśli nie można na niej polegać?

# Najpierw omówimy kilka podstawowych statystyk opisowych. Statystyka opisowa podsumowuje ważne cechy zbioru danych, takie jak:

#     Zliczanie
#     Suma
#     Odchylenie standardowe
#     Percentyl
#     Średnia
#     Itp..

# Jest to dobry punkt wyjścia do zapoznania się z danymi.
# We can use the describe() function in Python to summarize the data:

import pandas as pd

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

print (full_health_data.describe())

# Przykładowe dane wyjściowe (jedne z wielu, dla każdej kolumny):
#        Hours_Sleep  
# count   163.000000  
# mean      7.680982  
# std       0.663934  
# min       5.000000  
# 25%       7.500000  
# 50%       8.000000  
# 75%       8.000000  
# max      12.000000

###&&&___^___&&&### Data Science - Statistics Percentiles



###&&&___^___&&&### Data science - statistics variance

# Wariancja to kolejna liczba wskazująca, jak rozłożone są wartości.
# W rzeczywistości, jeśli weźmiemy pierwiastek kwadratowy z wariancji, otrzymamy odchylenie standardowe. 
# Lub odwrotnie, jeśli pomnożysz odchylenie standardowe przez samo odchylenie, otrzymasz wariancję!
# Najpierw użyjemy zestawu danych zawierającego 10 obserwacji, aby dać przykład, jak możemy obliczyć wariancję:

# <tabela z danymi>

# Tip: Variance is often represented by the symbol Sigma Square: σ^2

#& Step 1 to Calculate the Variance: Find the Mean

# Chcemy znaleźć średnią z kolumny Average_Pulse)
# (80+85+90+95+100+105+110+115+120+125) / 10 = 102.5 

#& Step 2: For Each Value - Find the Difference From the Mean

# 80 - 102.5 = -22.5
# 85 - 102.5 = -17.5
# 90 - 102.5 = -12.5
# 95 - 102.5 = -7.5
# 100 - 102.5 = -2.5
# 105 - 102.5 = 2.5
# 110 - 102.5 = 7.5
# 115 - 102.5 = 12.5
# 120 - 102.5 = 17.5
# 125 - 102.5 = 22.5 

#& Step 3: For Each Difference - Find the Square Value

# (-22.5)^2 = 506.25
# (-17.5)^2 = 306.25
# (-12.5)^2 = 156.25
# (-7.5)^2 = 56.25
# (-2.5)^2 = 6.25
# 2.5^2 = 6.25
# 7.5^2 = 56.25
# 12.5^2 = 156.25
# 17.5^2 = 306.25
# 22.5^2 = 506.25

# Note: we must square the values to get the total spread.

#& Step 4: The Variance is the Average Number of These Squared Values

# 4. Sum the squared values and find the average:
# (506.25 + 306.25 + 156.25 + 56.25 + 6.25 + 6.25 + 56.25 + 156.25 + 306.25 + 506.25) / 10 = 206.25

### Use Python to Find the Variance of health_data
# We can use the var() function from NumPy to find the variance:

import pandas as pd
import numpy as np

health_data = pd.read_csv("data.csv", header=0, sep=",")

var = np.var(health_data)
print(var)

### Use Python to Find the Variance of Full Data Set
import pandas as pd
import numpy as np

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

var = np.var(full_health_data)

print(var)

###&&&___^___&&&### Data Science - statistics correlation

# Korelacja mierzy związek między dwiema zmiennymi.
# Wspomnieliśmy, że funkcja ma na celu przewidywanie wartości poprzez konwersję danych wejściowych (x) na dane wyjściowe (f(x)). 
# Można powiedzieć, że funkcja wykorzystuje do przewidywania relację między dwiema zmiennymi.

# Współczynnik korelacji

# Współczynnik korelacji mierzy związek między dwiema zmiennymi.
# Współczynnik korelacji nigdy nie może być mniejszy niż -1 i wyższy niż 1.

#     1 = istnieje idealna liniowa zależność pomiędzy zmiennymi (np. Średnia_Pulse względem Spalenia Kalorii)
#     0 = nie ma liniowej zależności pomiędzy zmiennymi
#     -1 = istnieje idealna ujemna liniowa zależność między zmiennymi
#     (np. mniej przepracowanych godzin prowadzi do większego spalania kalorii podczas sesji treningowej)

# Przykład idealnej zależności liniowej (współczynnik korelacji = 1)
# Użyjemy wykresu rozrzutu do wizualizacji związku pomiędzy Average_Pulse i Calorie_Burnage 
# (użyliśmy małego zestawu danych zegarka sportowego z 10 obserwacjami).
# Tym razem chcemy wykresów punktowych, więc zmieniamy rodzaj na „rozpraszany”:

import matplotlib.pyplot as plt

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='scatter')
plt.show()

# For correlation coefficent: -1

import pandas as pd
import matplotlib.pyplot as plt

negative_corr = {'Hours_Work_Before_Training': [10,9,8,7,6,5,4,3,2,1],
'Calorie_Burnage': [220,240,260,280,300,320,340,360,380,400]}
negative_corr = pd.DataFrame(data=negative_corr)

negative_corr.plot(x ='Hours_Work_Before_Training', y='Calorie_Burnage', kind='scatter')
plt.show()

###&&&___^___&&&### Data Science - statistics correlation matrix

# Macierz to tablica liczb ułożonych w wiersze i kolumny.
# Macierz korelacji to po prostu tabela pokazująca współczynniki korelacji pomiędzy zmiennymi.

# <tabela z danymi dostępna w module>

# W powyższej tabeli wykorzystano dane z pełnego zestawu danych dotyczących zdrowia.

# Obserwacje:

#     Zauważamy, że czas trwania i spalanie kalorii są ze sobą ściśle powiązane, a współczynnik korelacji wynosi 0,89. 
#     Ma to sens, ponieważ im dłużej trenujemy, tym więcej kalorii spalamy
#     Obserwujemy, że prawie nie ma liniowej zależności pomiędzy Average_Pulse i Calorie_Burnage (współczynnik korelacji 0,02)
#     Czy możemy stwierdzić, że Average_Pulse nie wpływa na Calorie_Burnage? Nie. Wrócimy, aby odpowiedzieć na to pytanie później!

### Correlation matrix in Python
# Możemy użyć funkcji corr() w Pythonie, aby utworzyć macierz korelacji. 
# Używamy również funkcji round(), aby zaokrąglić wynik do dwóch miejsc po przecinku:

import pandas as pd

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

corr_matrix = round(full_health_data.corr(),2)

print(corr_matrix)

### Using a heatmap - use Seaborn to creata a heatmap

# Możemy użyć biblioteki Seaborn do stworzenia mapy cieplnej korelacji (Seaborn to biblioteka wizualizacyjna oparta na matplotlib):

import matplotlib.pyplot as plt
import seaborn as sns 

correlation_full_health = full_health_data.corr()

axis_corr = sns.heatmap(
    correlation_full_health,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(50,500,n=500),
    square=True)

plt.show()

# Wyjasnienie:
    
# Zaimportuj bibliotekę seaborn jako sns.
# Użyj zestawu full_health_data.
# Użyj sns.heatmap(), aby poinformować Pythona, że ​​chcemy, aby mapa cieplna wizualizowała macierz korelacji.
# Skorzystaj z macierzy korelacji. Zdefiniuj maksymalne i minimalne wartości mapy cieplnej. Zdefiniuj, że 0 jest środkiem.
# Zdefiniuj kolory za pomocą sns.diverging_palette. n=500 oznacza, że ​​chcemy mieć 500 rodzajów kolorów w tej samej palecie barw.
# kwadrat = True oznacza, że ​​chcemy widzieć kwadraty.


###&&&___^___&&&### Data Science - statistics correlation vs causality






























