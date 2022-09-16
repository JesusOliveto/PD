/* Definir la relación resto(L1,L2) donde se verifique si L2 es la lista obtenida de L1, eliminando el primer elemento.

Pruebas:

resto([a,b,c],L).

L = [b,c] */

resto([_|L],L).

/* Definir la relación de pertenencia(X,L) donde se verifique si X es un elemento de la lista L.

Pruebas:

pertenencia(b,[a,b,c]).

true

pertenencia(d,[a,b,c]).

false */

pertenencia(X,[X|_]).
pertenencia(X,[_|L]) :- pertenencia(X,L).

/* Determinar el tamaño de una lista L.

Pruebas:

size([1,2,3],L).

L=3

Size([],L).

L=0 */

size([],0).
size([_|L],N) :- size(L,N1), N is N1+1.

/* Definir la relación iguales(L), que valide si todos los valores de la lista L son iguales.

Pruebas:

iguales([a,a,a]).

true

iguales[a,b,c]).

false

Iguales([]).

true */

iguales([]).
iguales([_]).
iguales([X,X|L]) :- iguales([X|L]).
iguales([X,Y|L]) :- X \= Y, iguales([Y|L]).

/* Definir la relación mayor(X,Y,Z) que valide en Z cual es el mayor entre X e Y.

Pruebas:

mayor(4,5,Z).

Z=5

mayor(7,2,Z).

Z=7 */

mayor(X,Y,X) :- X >= Y.
mayor(X,Y,Y) :- X < Y.

/* Definir la relación sumLista(L,X) donde X sea la suma de los elementos de la lista L.

Pruebas:

sumLista([1,2,3],X).

X=6 */

sumLista([],0).
sumLista([X|L],S) :- sumLista(L,S1), S is S1+X.

/* Definir la relación orden(L) que verifique si la lista L esta ordenada en forma ascendente.

Pruebas:

orden([1,3,4,6]).

True

orden([1,6,5,2]).

False */

orden([]).
orden([_]).
orden([X,Y|L]) :- X =< Y, orden([Y|L]).

/* Definir la relación listaNum(N,M,L) que devuelva L como la lista de valores desde N hasta M

Pruebas:

listaNum(3,6,L).

L = [3,4,5,6]

listaNum(3,1,L).

false */

listaNum(N,N,[N]).
listaNum(N,M,[N|L]) :- N < M, N1 is N+1, listaNum(N1,M,L).

/* Definir una función que inserte un valor en una lista ordenada en forma ascendente de tal forma que el valor quede en el lugar que le corresponda.

Pruebas:

insert(1,[],L).

L=[1]

insert(3,[1,2,4,5],L).

L=[1,2,3,4,5] */

insert(X,[],[X]).
insert(X,[Y|L],[X,Y|L]) :- X =< Y.
insert(X,[Y|L],[Y|L1]) :- X > Y, insert(X,L,L1).

/* Definir una función que indique si los valores ingresados forman un capicúa.

Pruebas:

capicua([o,s,o]).

True

capicua([1,2,1]).

True

capicua([1,2,3]).

false */

capicua([]).
capicua([_]).
capicua([X|L]) :- ultimo(L,X), resto(L,L1), capicua(L1).

ultimo([X],X).
ultimo([_|L],X) :- ultimo(L,X).

resto([_|L],L).

