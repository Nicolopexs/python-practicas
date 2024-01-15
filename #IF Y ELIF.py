#IF Y ELIF
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

#CALCULAR IMC
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


