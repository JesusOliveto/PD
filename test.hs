cuadrado::Integer->Integer
cuadrado x = x * x

impar::Integer->Bool
impar x = mod x 2 == 1

parTexto::Integer->String
parTexto x = if (mod x 2 == 0) then "par" else "impar"

menor::(Integer,Integer)->Bool
menor (x,y) = if (x<=y) then True else False

abs::Integer->Integer
abs x = if (x<0) then (-x) else x

signnum::Integer->Integer
signnum x = if (x>0) then 1 else if (x<0) then -1 else 0

anterior::Integer->Integer
anterior x= if (x>0) then x-1 else error "No hay anterior"

siguiente::Integer->Integer
siguiente x=x+1

doble::Integer->Integer
doble x=x*2

filterPositivos::[Integer]->[Integer]
filterPositivos xs = filter (>0) xs
