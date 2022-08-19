--clase 1
cuadrado::Integer->Integer
cuadrado x = x * x

impar::Integer->Bool
impar x = mod x 2 == 1

parTexto::Integer->String
parTexto x = if (mod x 2 == 0) then "par" else "impar"

menor::(Integer,Integer)->Bool
menor (x,y) = if (x<=y) then True else False

--EJERCITACION

absoluto::Integer->Integer
absoluto x = if (x<0) then (-x) else x

signumRedef::Integer->Integer
signumRedef x = if (x>0) then 1 else if (x<0) then -1 else 0

anterior::Integer->Integer
anterior x= if (x>0) then x-1 else error "No hay anterior"

siguiente::Integer->Integer
siguiente x=x+1

doble::Integer->Integer
doble x=x*2

filterPositivos::[Integer]->[Integer]
filterPositivos xs = filter (>0) xs

filterPositivosRec::[Integer]->[Integer]
filterPositivosRec [] = []
filterPositivosRec (x:xs) = if (x>0) then x:filterPositivosRec xs else filterPositivosRec xs

--FIN EJERCITACION

--clase 2
add::Integer->Integer->Integer
add x y = x+y
main = do 
    putStrLn "Ingrese un numero"
    numero <- getLine
    putStrLn "Ingrese otro numero"
    numero2 <- getLine
    putStrLn "El resultado es: "
    print (add (read numero) (read numero2))

--clase 3
suma::[Integer]->Integer
suma [] = 0
suma (x:xs) = x + suma xs

--quicksort 
quicksort::[Integer]->[Integer]
--quicksort [] = []
quicksort (x:xs) = quicksort [y | y <- xs, y<x] ++ [x] ++ quicksort [y | y <- xs, y>=x]

fibonacci::Integer->Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)

describeList::[Integer]->String
describeList xs = "La lista es " ++ case xs of [] -> "vacia"
                                               [x] -> "una lista de un solo elemento"
                                               xs -> "una lista con " ++ show (length xs) ++ " elementos"


