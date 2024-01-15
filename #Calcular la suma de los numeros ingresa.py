#Calcular la suma de los numeros ingresados ingresados por teclado sumar y hallar la media

numeros = input("Ingrese los numeros: ")
numeros = numeros.split(" ")

numeroscadena = [int(enteros) for enteros in numeros]

suma = sum(numeroscadena)

media = suma/len(numeros)

print("Respuesta: ")
print("La suma de los numeros es: ", suma)
print("La media los numeros es: ",media)
