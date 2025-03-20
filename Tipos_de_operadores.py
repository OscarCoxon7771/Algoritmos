'''
Operadores en Python
'''

#Suma
x=2+6
print(x)

#Resta
y=8-2
print(y)

#Multiplicación
print(2*25)


#División
''' Para python la división siempre será flotante'''
divide=25/5
print(divide)
print(type(divide))



#División piso (Floor Division)
''' La división piso siempre será el entero más cercano hacia abajo'''
print(10/3)
print(10//3)

print(4/3)
print(4//3)

print(14.5/3)
print(14.5//3)


'''
Pruebe realizar la operación piso 8//-3 y compare con 8/-3
'''
print(8//-3)
print(8/-3)


#Módulo(Residuo)
w=20/3
y=20%3

print(w)
print(y)

print(type(y))


#Potencia
print(2**3)

'''
Operadores de comparación
'''

#Igualdad

print("x"=="X")
print(3==3.0)
print(3==3.00000001)

#Desigualdad
print(4!=5)
print(False != True)

#incremento


#decrecimiento

y=5
y=y-1
y-=1
print(y)

#asigna multiplicación


'''
Operadores lógicos
and
or
not
'''

print(x==4 and y==4)

x=4 #Defino el valor
x==4 #Prengunto si x es igual a 4
y=4

print(x==4 and y==4)

print(x==4 or y==2) #Solo una de las dos condiciones se cumple


#Uso de not
'''
En el caso del operador not se valida si la condición es falsa'''

print(not x)

enunciado=True
print(not enunciado)

enunciado2=False
print(not enunciado2)

usuario_logueado=True
boton_logout=True
print(not usuario_logueado)