# Autor: Oscar El Coxon
# Este es un cmentario de una sola línea'
'''
Este tambiés es un comentario en varias
líneas
'''

print("Estudiando Python")

# Definición de variables
'''
reglas:
Python es sensible a mayúsculas y minúsculas
No se pueden usar espacios en los nombres de las variables
No se pueden usar palabras reservadas
No es conveniente usar números como nombres de variables
'''

x=50
y=15

print(x+y)

print(type(x))
# <class 'int'> : significa que x es un número entero}
nombre="Oscar"
print(nombre)
print(type(nombre))
# <class 'str'> : significa que la variable nombre es una cadena de texto (String)

print(type(x))
x=4.8
print(type(x))
# <class 'float'> : significa que x es un número decimal

# print(type(x+nombre))
# <class 'str'> : significa que el resultado de la suma de x y nombre no es posible

print(x , nombre)