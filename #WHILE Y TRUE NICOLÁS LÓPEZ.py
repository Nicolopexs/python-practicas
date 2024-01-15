#WHILE Y TRUE

#SERIE DE FIBONACCI

inicio = int(input("Ingrese desde qué número quiere: "))
hasta = int(input("Ingrese hasta qué número quiere: "))


s = inicio
k = inicio

print(inicio)

while s < hasta:
    
    s = inicio + k
    #el valor de inicio se guarda en k
    inicio = k
    #y k se guarda en s
    k = s
    #imprimimos s
    print(s)


#Numero factorial
numero = int(input("Ingrese un número: "))
numeros_generados = []

while numero > 0:
    numeros_generados.append(numero)
    numero -= 1

producto = 1
indice = 0
tamaño = len(numeros_generados)

while indice < tamaño:
    #producto vale 1 para multiplicar con cada uno de los numeros por ejemplo 1*4 = 4 el cuatro se almacena en producto
    #y ahora 4 va a multiplicarse por el siguiente numero 4*5=20 y asi sucesivamente
    producto *= numeros_generados[indice]
    indice += 1

print("Producto:", producto)
""""" 


#Ingresar n números por el teclado, y realizar el conteo de los números pares e impares

numero2 = int(input("Ingrese un número: "))
numeros_generados2 = []

while numero2 > 0:
    numeros_generados2.append(numero2)
    numero2 -= 1

numeros_pares = []
numeros_impares = []
indice2 = 0
tamaño2 = len(numeros_generados2)

while indice2 < tamaño2:

    numero_actual = numeros_generados2[indice2]

    if numero_actual % 2 == 0:
        numeros_pares.append(numero_actual)
    else:
        numeros_impares.append(numero_actual)

    indice2 += 1

print("Números pares:", len(numeros_pares))
print("Números impares:", len(numeros_impares))



