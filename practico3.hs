import Data.List

--1) Redefinir la función map de tal forma que map f lista-> devuelva la lista obtenida aplicando f a cada elemento de lista. 
--Hacer dos versiones de la funcion:
--aplicando recursividad 
--aplicado listas intensionales

--Ejemplo:
--map' (3*) [1,2,3] -> [3,6,9]

map1 :: (a->b) -> [a] -> [b]
map1 f [] = []
map1 f (x:xs) = f x : map1 f xs

map2 :: (a->b) -> [a] -> [b]
map2 f xs = [f x | x <- xs]

--2)Redefinir la función sum de tal forma que sum de lista -> devuelva la suma de los elementos de lista. 

--Ejemplo:
--sum' [1,3,6] -> 10

sum1 :: Num a => [a] -> a
sum1 [] = 0
sum1 (x:xs) = x + sum1 xs

--3)Definir una función que tome dos listas xs ys  y verifica si las dos listas xs e ys son iguales, devuelve True si son iguales sino False. 

iguales :: Eq a => [a] -> [a] -> Bool
iguales [] [] = True
iguales (x:xs) (y:ys) = x == y && iguales xs ys
iguales _ _ = False

--4)Definir una funcion tal forma que sume de los cuadrados de los elementos de la lista l. 

--Por ejemplo:
--sum_cuadrados [1,2,3] -> 14

sum_cuadrados :: Num a => [a] -> a
sum_cuadrados [] = 0
sum_cuadrados (x:xs) = x^2 + sum_cuadrados xs

--5)Redefinir la función filter de tal forma que filter' p lista -> devuelva la lista de los elementos de lista que cumplen la propiedad p. Por ejemplo,
--filter even [1,2,3,4,5,6,7] -> [2,4,6]
--filter (>3) [1,2,3,5,6,7] -> [5,6,7]

filter1 :: (a->Bool) -> [a] -> [a]
filter1 p [] = []
filter1 p (x:xs) | p x = x : filter1 p xs
                 | otherwise = filter1 p xs

--6)Redefinir la función head de tal forma que head' lista es el head de lista. 
--Por ejemplo:
--head [3,5,2] -> 3 
--head [] -> "Error lista vacia"

head1 :: [a] -> a
head1 [] = error "Lista vacia"
head1 (x:xs) = x

--7)Definir una función que reciba una lista como parámetro y devuelta true si la lista tiene valores repetidos y false en caso contrario
--Ejemplo:
--duplicados [1,2,3,4] -> false
--duplicados [1,2,3,2] -> true

duplicados :: Eq a => [a] -> Bool
duplicados [] = False
duplicados (x:xs) = elem x xs || duplicados xs

--8)Definir una funcion que reciba una lista y valide si la lista esta ordenada de menor a mayor, si lo cumple devuelve true sino false

ordenada :: Ord a => [a] -> Bool
ordenada [] = True
ordenada [x] = True
ordenada (x:y:xs) = x <= y && ordenada (y:xs)

--9)Definir una función que calcule el valor mayor de tres pasados como parametros 
--Por ejemplo:
--mayor 6 2 4 == 6
--mayor 6 7 4 == 7
--mayor 6 7 9 == 9

mayor :: Ord a => a -> a -> a -> a
mayor x y z = max x (max y z)

--10)Definir una función que reciba una lista como parámetro y devuelva otra lista de tal forma que el primer elemento de la lista sea el ultimo en la lista resultante
--Ejemplo

--cambiar [1,2,3] -> [2,3,1]

cambiar :: [a] -> [a]
cambiar [] = []
cambiar (x:xs) = xs ++ [x]
