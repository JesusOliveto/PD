import random

""" 1) ingresar por teclado una cantidad. Esa cantidad indicara cuantos valores ingresar.
Calcular el promedio de los valores ingresado """

def promedio():
    cant = int(input("ingrese la cantidad de valores: "))
    suma = 0
    for i in range(cant):
        valor = int(input("ingrese un valor: "))
        suma += valor
    prom = suma/cant
    print("el promedio es: ", prom)

""" 2) Crear un algoritmo que reciba tres valores que seran cantidad de respuestas correctas, cantidad de respuestras incorrectas
y cantidad de respuestas en blanco.
Cada respuesta correcta tiene un puntaje de 5, cada incorrecta tiene un puntaje de -1 y las respuestas en blanco 0.
Calcular el puntaje para cada tipo de respuesta y el puntaje total. """

def puntaje():
    correctas = int(input("ingrese la cantidad de respuestas correctas: "))
    incorrectas = int(input("ingrese la cantidad de respuestas incorrectas: "))
    blancas = int(input("ingrese la cantidad de respuestas en blanco: "))
    puntaje_correctas = correctas * 5
    puntaje_incorrectas = incorrectas * -1
    puntaje_blancas = blancas * 0
    puntaje_total = puntaje_correctas + puntaje_incorrectas + puntaje_blancas
    print("el puntaje total es: ", puntaje_total)

""" 3)Ingresar por teclado 20 números enteros y calcular cuántos de ellos son pares. Se emprime el resultado. """

def pares():
    pares = 0
    for i in range(20):
        numero = int(input("ingrese un numero: "))
        if numero % 2 == 0:
            pares += 1
    print("la cantidad de numeros pares es: ", pares)

""" 4)Ingresar cantidad de numeros, generar esa cantidad en forma aleatoria de numeros enteros positivos , 
y determinar cuantos son impares. """

def impares():
    cant = int(input("ingrese la cantidad de numeros: "))
    impares = 0
    for i in range(cant):
        numero = random.randint(0, 100)
        if numero % 2 != 0:
            impares += 1
    print("la cantidad de numeros impares es: ", impares)

""" 5)Escriba un algoritmo tal que dado como datos X números
enteros, obtenga el número de ceros que hay entre estos
números. Por ejemplo, si se ingresa 6 datos: 9 0 4 8 0 1
El algoritmo arroja que hay 2 ceros. """

def ceros():
    cant = int(input("ingrese la cantidad de numeros: "))
    ceros = 0
    for i in range(cant):
        numero = int(input("ingrese un numero: "))
        if numero == 0:
            ceros += 1
    print("la cantidad de ceros es: ", ceros)

""" 6)Ingresar 50 caracteres e indicar cuantas veces se repite el carácter ‘a’.  """

def a():
    cant = 0
    for i in range(50):
        caracter = input("ingrese un caracter: ")
        if caracter == "a":
            cant += 1
    print("la cantidad de veces que se repite la letra a es: ", cant)

""" 7)Se tiene N temperaturas. Se desea calcular su media y
determinar entre todas ellas cuantas son superiores o iguales a
esa media. """

def temperaturas():
    cant = int(input("ingrese la cantidad de temperaturas: "))
    vector = []
    suma = 0
    for i in range(cant):
        temperatura = int(input("ingrese una temperatura: "))
        vector.append(temperatura)
        suma += temperatura
    promedio = suma / cant
    mayores = 0
    for i in range(len(vector)):
        if vector[i] >= promedio:
            mayores += 1
    print("el promedio es: ", promedio)
    print("la cantidad de temperaturas mayores o iguales al promedio es: ", mayores)



""" 8)Escribir un algoritmo que pida un vector de caracteres por
pantalla e invierta el orden de los caracteres mostrándolo por
pantalla.  """

def invertir():
    palabra = input("ingrese una palabra: ")
    palabra_invertida = palabra[::-1]
    print("la palabra invertida es: ", palabra_invertida)
    
""" 9)Realizar un algoritmo que maneje un vector de enteros a través
de un menú con seis opciones:
1.- Añadir un elemento al vector (comprobando que el vector
no esté lleno)
2.- Eliminar un elemento del vector (comprobando que el
vector no esté vacío)
3.- Listar el contenido del vector
4.- Contar las apariciones de un número en el vector
5.- Calcular la media y el máximo de los elementos del vector
0.- Terminar """

def menu():
    vector = []
    opcion = 1
    while opcion != 0:
        print("1.- Añadir un elemento al vector")
        print("2.- Eliminar un elemento del vector")
        print("3.- Listar el contenido del vector")
        print("4.- Contar las apariciones de un número en el vector")
        print("5.- Calcular la media y el máximo de los elementos del vector")
        print("0.- Terminar")
        opcion = int(input("ingrese una opcion: "))
        if opcion == 1:
            if len(vector) == 10:
                print("el vector esta lleno")
            else:
                numero = int(input("ingrese un numero: "))
                vector.append(numero)
        elif opcion == 2:
            if len(vector) == 0:
                print("el vector esta vacio")
            else:
                numero = int(input("ingrese un numero: "))
                vector.remove(numero)
        elif opcion == 3:
            print(vector)
        elif opcion == 4:
            numero = int(input("ingrese un numero: "))
            cant = 0
            for i in range(len(vector)):
                if vector[i] == numero:
                    cant += 1
            print("la cantidad de veces que se repite el numero es: ", cant)
        elif opcion == 5:
            suma = 0
            maximo = 0
            for i in range(len(vector)):
                suma += vector[i]
                if vector[i] > maximo:
                    maximo = vector[i]
            prom = suma/len(vector)
            print("el promedio es: ", prom)
            print("el maximo es: ", maximo)
        elif opcion == 0:
            print("terminando")
        else:
            print("opcion incorrecta")
            
""" 10)Elaborar algoritmo que busque en forma secuencial un
VALOR dentro de un arreglo de N elementos numéricos y
retorne su posición.  """

def busqueda():
    vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numero = int(input("ingrese un numero: "))
    posicion = -1
    for i in range(len(vector)):
        if vector[i] == numero:
            posicion = i
    if posicion == -1:
        print("el numero no se encuentra en el vector")
    else:
        print("el numero se encuentra en la posicion: ", posicion)
        
""" 11)Cargar un vector de 25 posiciones con numero enteros, a
partir de este crear 2 vectores; uno con los números pares y el
otro con los numero impares, además decir de los vectores
cual es más grande y el número de elementos en cada vector.  """

def pares_impares():
    vector = []
    for i in range(25):
        numero = int(input("ingrese un numero: "))
        vector.append(numero)
    vector_pares = []
    vector_impares = []
    for i in range(len(vector)):
        if vector[i] % 2 == 0:
            vector_pares.append(vector[i])
        else:
            vector_impares.append(vector[i])
    print("el vector de pares es: ", vector_pares)
    print("el vector de impares es: ", vector_impares)
    if len(vector_pares) > len(vector_impares):
        print("el vector de pares es mayor")
    else:
        print("el vector de impares es mayor")
    print("la cantidad de elementos del vector de pares es: ", len(vector_pares))
    print("la cantidad de elementos del vector de impares es: ", len(vector_impares))

""" 12)Se tiene un vector, se pide ingresar 20 nombres de animales,
luego se debe buscar el nombre de un animal que se ingrese
por teclado, el algoritmo debe imprimir el nombre de los
animales que se encuentran al lado de la posición donde está
el animal buscado, tanto a la derecha como izquierda. """

def animales():
    vector = []
    for i in range(20):
        animal = input("ingrese un animal: ")
        vector.append(animal)
    animal = input("ingrese un animal a buscar: ")
    for i in range(len(vector)):
        if vector[i] == animal:
            if i == 0:
                print("el animal a la derecha es: ", vector[i+1])
            elif i == len(vector)-1:
                print("el animal a la izquierda es: ", vector[i-1])
            else:
                print("el animal a la derecha es: ", vector[i+1])
                print("el animal a la izquierda es: ", vector[i-1])




promedio()
puntaje()
pares()
impares()
ceros()
a()
temperaturas()
invertir()
menu()
busqueda()
pares_impares()
animales()