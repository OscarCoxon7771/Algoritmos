
#Ejercicio 1.5

'''
Escriba un programa que realice la comprobación
de la división. Recuerde:
Divisor * Cociente + Residuo = Dividendo
Tome como entrada dos números, realice la
división entre ellos y entregue al usuario un texto
descriptivo con la comprobación de la división.
'''

dividendo=int(input("Ingrese el dividendo: "))
divisor=int(input("Ingrese el divisor: "))

#Calcular
cociente=dividendo/divisor
residuo=dividendo%divisor

print(f"El cociente es: {divisor} por {cociente} más {residuo} es igual a {dividendo}.")