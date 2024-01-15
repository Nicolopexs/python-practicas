
texto = input("Ingresa una palabra o frase: ")

def es_palindromo(texto):
    
    texto = texto.replace(" ", "").lower()
    
    return texto == texto[::-1]

if es_palindromo(texto):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
