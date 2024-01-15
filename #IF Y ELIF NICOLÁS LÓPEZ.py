#IF Y ELIF

#CALCULAR IMC

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print("Su IMC es: %.2f" %imc)


if imc < 18.5:
        print("Usted tiene Bajo peso") 
elif imc < 25:
        print("Usted tien Peso normal")
elif imc < 30:
        print("Usted tiene Sobrepeso (Obesidad grado 1)") 
elif imc < 35:
        print("Usted Sobrepeso (Obesidad grado 2)")
else:
        print("Usted tiene Sobrepeso (Obesidad grado 3)")

      
# Verificar si aprueba, va a supletorio o pierde la materia

nota_parcial1 = float(input("Ingrese la nota del primer parcial: "))
nota_parcial2 = float(input("Ingrese la nota del segundo parcial: "))

nota1 = nota_parcial1 * 0.35
nota2 = nota_parcial2 * 0.35
final2 = nota1 + nota2

if final2 >= 7:
    print("El estudiante aprueba la materia de POO II.")
elif final2 < 4:
    print("El estudiante pierde la materia de POO II.")

else:
    nota_supletorio = float(input("Ingrese la nota del supletorio: "))

    nota3 = nota_supletorio * 0.30
    final = final2 + nota3

    if final >= 7:
        print("El estudiante aprueba la materia de POO II mediante el supletorio.")
    else:
        print("El estudiante pierde la materia de POO II.")


#Verficar si la contraseña es segura

contrasena = input("Ingrese una contraseña: ")

if len(contrasena) < 8:
    print("La contraseña no cumple con la longitud mínima de 8 caracteres.")
elif not any(c.isupper() for c in contrasena):
    print("La contraseña debe contener al menos una letra mayúscula.")
elif not any(c.islower() for c in contrasena):
    print("La contraseña debe contener al menos una letra minúscula.")
elif not any(c.isdigit() for c in contrasena):
    print("La contraseña debe contener al menos un número.")
elif not any(c in "!@#$%^&*()" for c in contrasena):
    print("La contraseña debe contener al menos un símbolo especial.")
else:
    print("La contraseña es segura.")

