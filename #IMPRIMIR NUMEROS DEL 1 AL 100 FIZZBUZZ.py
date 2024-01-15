#IMPRIMIR NUMEROS DEL 1 AL 100 PERO REMPLAZARLOS POR PALABRAS

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#EUCLIDES
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

a, b = num1, num2

#PARA ENCONTRAR EL VALOR MINUMO DE DOS O MAS VALORES
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        mcd = i
        break

print("El máximo común divisor de", num1, "y", num2, "es:", mcd)

#PROGRAMA QUE PERMITA IMPRIMIR TODOS LOS NUMEROS PRIMOS DE UN NUMERO ENTERO
num = int(input("Ingrese un número entero: "))

print("Números primos hasta", num, "son:")

#si "num" es igual a 5, la secuencia generada sería [2, 3, 4, 5].

for i in range(2, num + 1):
    #"es_primo" en 1 para indicar que asumimos inicialmente que "i" es primo.
    es_primo = 1
    for j in range(2, i):
        #si "i % j == 0 
        if i % j == 0:
            es_primo = 0
            break
    if es_primo:
        print(i)



