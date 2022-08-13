cuadrado::Integer->Integer
cuadrado x = x * x

impar::Integer->Bool
impar x = mod x 2 == 1

parTexto::Integer->String
parTexto x = if (mod x 2 == 0) then "par" else "impar"
