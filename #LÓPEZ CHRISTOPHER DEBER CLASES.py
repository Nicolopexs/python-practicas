#PALINDROMO
class Palindromo:
    #
    def __init__(self, texto):
        self.texto = texto

    def es_palindromo(self):
        texto_limpio = self.texto.replace(" ", "").lower()

        if texto_limpio == texto_limpio[::-1]:
            return "ES PALINDROMO"
        else:
            return "NO ES PALINDROMO"

t = input("Ingrese una cadena de texto: ")
#instancia
palindromo = Palindromo(t)

print(palindromo.es_palindromo())


#FACTORIAL
class Factorial:
    def __init__(self, n):
        self.n = n

    def calcular_factorial(self):
        factorial = 1
        for i in range(1, self.n + 1):
            factorial = factorial * i
        return factorial


numero = int(input("Ingrese un número: "))

factorial_ = Factorial(numero)

print("El factorial de", numero, "es:", factorial_.calcular_factorial())


#FIBONACCI 

class Fibonacci:
    def __init__(self, h):
        self.h = h
        self.s = 0
        self.f = 0
        self.k = 1

    def serie(self):
        print(self.k)
        while self.s < self.h:
            
            self.s = self.f + self.k
            self.f = self.k
            self.k = self.s

            print(self.s)

h = int(input("INGRESE UN NUMERO: "))

fibonacci = Fibonacci(h)

print("La serie de Fibonacci es:")
fibonacci.serie()


