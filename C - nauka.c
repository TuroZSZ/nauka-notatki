/* C - nauka*/

/* Learn C
C is a general-purpose programming language that has been widely used for over 50 years.
C is very powerful; it has been used to develop operating systems, databases, applications, etc.*/

/* Przykład kodu */

#include <stdio.h>
 int main() {
    printf("Hello World!");
    return 0;
 }


/* Co to jest C?

C to język programowania ogólnego przeznaczenia stworzony przez Dennisa Ritchiego w Bell Laboratories w 1972 roku.
Jest to bardzo popularny język, mimo że jest stary. Głównym powodem jego popularności jest to, że jest to podstawowy język w dziedzinie informatyki.
Język C jest silnie powiązany z systemem UNIX, ponieważ został opracowany w celu napisania systemu operacyjnego UNIX. */

/* Dlaczego warto uczyć się C?

   - Jest to jeden z najpopularniejszych języków programowania na świecie
   - Jeśli znasz C, nie będziesz mieć problemu z nauką innych popularnych języków programowania, 
    takich jak Java, Python, C++, C# itp., ponieważ składnia jest podobna
   - C jest bardzo szybki w porównaniu do innych języków programowania, takich jak Java i Python
   - C jest bardzo wszechstronny; można go stosować zarówno w aplikacjach, jak i technologiach

Różnica między C i C++

    C++ został opracowany jako rozszerzenie C i oba języki mają prawie taką samą składnię
    Główna różnica między C i C++ polega na tym, że C++ obsługuje klasy i obiekty, podczas gdy C nie */


/* ### C Syntax ###                 */

#include <stdio.h>

int main() {
   printf("Hello World!");
   return 0;
}

/* Wyjaśnienie przykładu:

Linia 1: #include <stdio.h> to biblioteka plików nagłówkowych, która pozwala nam pracować z funkcjami wejściowymi 
i wyjściowymi, takimi jak printf() (używana w linii 4). Pliki nagłówkowe dodają funkcjonalność do programów C.

Nie martw się, jeśli nie rozumiesz, jak działa #include <stdio.h>. Pomyśl o tym jak o czymś, 
co (prawie) zawsze pojawia się w Twoim programie.

Linia 2: Pusta linia. C ignoruje białe znaki. Ale używamy go, aby uczynić kod bardziej czytelnym.

Linia 3: Kolejną rzeczą, która zawsze pojawia się w programie C, jest funkcja main(). 
Nazywa się to funkcją. Każdy kod znajdujący się w nawiasach klamrowych {} zostanie wykonany.

Linia 4: printf() to funkcja używana do wyprowadzania/drukowania tekstu na ekranie. 
W naszym przykładzie wyświetli się „Hello World!”.

Zauważ, że: Każda instrukcja C kończy się średnikiem;

Uwaga: Treść funkcji int main() można również zapisać jako:
int main(){printf("Hello, World!");return 0;}

Pamiętaj: Kompilator ignoruje białe spacje. Jednak wiele linii sprawia, że ​​kod jest bardziej czytelny.

Linia 5: return 0 kończy funkcję main().

Linia 6: Nie zapomnij dodać zamykającego nawiasu klamrowego }, aby faktycznie zakończyć funkcję główną.
 */


/* ### C Statements ###                 */

/* A computer program is a list of "instructions" to be "executed" by a computer.
In a programming language, these programming instructions are called statements.
The following statement "instructs" the compiler to print the text "Hello World" to the screen: */


#include <stdio.h>

int main() {
   printf("Hello World!");
   return 0;
}

/* It is important that you end the statement with a semicolon ;
If you forget the semicolon (;), an error will occur and the program will not run */

/* # Many statements 
Most C programs contain many statements.
The statements are executed, one by one, in the same order as they are written:*/

#include <stdio.h>

int main() {
   printf("Hello, World!");
   printf("Have a good day!");
   return 0;
}

/* Explaination
The first statement is executed first (print "Hello World!" to the screen).
Then the second statement is executed (print "Have a good day!" to the screen).
And at last, the third statement is executed (end the C program successfully).*/

/* ### C Output (Print text)
To output values or print text in C, you can use the printf() function.

When you are working with text, it must be wrapped inside double quotations marks "".
If you forget the double quotes, an error occurs.

# Many prinf functions
Można dodać tyle funkcji printf ile się chce. Natomiast każda kolejna nie spowoduje, 
że powstanie nowy wiersz.
*/

#include <stdio.h>

int main() {
   printf("Temeria.");
   printf("Redania.");
   printf("Nilfgaard.");
   return 0;
} /* Wyjście: Temeria.Redania.Nilfgaard. */

/* ### C - New Lines 
Aby dodać nowe wiersze możemy użyć znaku \n */

#include <stdio.h>

int main() {
   printf("Hello world\n");
   printf("I'm learning C.");
   return 0;
}

/* Możliwe jest także zapisanie kilku linii w jednej funkcji printf() natomiast
może to być niewygodne do czytania. */

#include <stdio.h>

int main() {
   printf("Hello World\nI am learning C.\nI hope it will get me $$$.");
   return 0;
}

/* Dwa znaki \n\n dodadzą nam pustą linię pomiędzy wierszami tekstu: */

#include <stdio.h>

int main() {
   printf("Hello world!\n\n");
   printf("I am learning C");
   return 0;
}

/* Co to jest dokładnie \n ?
Znak nowej linii (\n) nazywany jest sekwencją ucieczki i zmusza kursor do zmiany pozycji na początek następnej linii na ekranie. W rezultacie powstaje nowa linia.
Przykłady innych prawidłowych sekwencji ucieczki to:

\t 	Creates a horizontal tab
\\ 	Inserts a backslash character (\)
\" 	Inserts a double quote character
*/

/* ### C Comments 
Comments can be used to explain code, and to make it more readable. It can also be used to prevent execution when testing alternative code.
Comments can be singled-lined or multi-lined.

# Single-line comments

Komentarze jednolinijkowe możemy zapisać przez podwójny ukośnikL // 
Np:
// komentarz do funkcji. 

# Multi-lines comments

Tak jak w tych notatkach: 
/* Komentarz */

// ### C Variables






