def es_paréntesis_balanceados(expresión):
    # Creamos una pila vacía que utilizaremos para rastrear los paréntesis de apertura.
    pila = []

    # Definimos un diccionario que contiene las parejas de paréntesis válidas.
    parejas = {')': '(', ']': '[', '}': '{'}

    # Iteramos sobre cada carácter en la expresión proporcionada.
    for carácter in expresión:
        # Si el carácter es un paréntesis de apertura, lo agregamos a la pila.
        if carácter in '({[':
            pila.append(carácter)
        # Si el carácter es un paréntesis de cierre, verificamos si coincide con el paréntesis superior en la pila.
        elif carácter in ')}]':
            # Si la pila está vacía o el paréntesis superior en la pila no coincide con el paréntesis de cierre actual,
            # entonces la expresión no está balanceada, retornamos False.
            if not pila or pila[-1] != parejas[carácter]:
                return False
            # Si coincide con el paréntesis de cierre, lo eliminamos de la pila.
            pila.pop()

    # Después de recorrer toda la expresión, si la pila está vacía, eso significa que todos los paréntesis están correctamente balanceados.
    # Retornamos True, en caso contrario, si quedaron paréntesis de apertura sin su par de cierre, retornamos False.
    return not pila

def main():
    print("Verificación de paréntesis en una expresión matemática.")
    while True:
        # Pedimos al usuario que ingrese una expresión o la palabra 'salir' para terminar el programa.
        expresión = input("Ingrese la expresión (o 'salir' para terminar): ")
        if expresión.lower() == 'salir':
            break

        # Llamamos a la función es_paréntesis_balanceados para verificar si los paréntesis están correctamente balanceados.
        if es_paréntesis_balanceados(expresión):
            print("Los paréntesis están correctamente balanceados en la expresión.")
        else:
            print("Los paréntesis NO están correctamente balanceados en la expresión.")

    print("¡Hasta luego!")

if __name__ == "__main__":
    main()
