'''
TIPOS DE DATOS
<class 'int'> : Identifica que la variable es un entero
<class 'float'> : Identifica la variable que es un numero decimal
<class 'str'> : Identifica que la variable es una cadena de texto
<class 'bool'>: Identifica que la variable es un valor True o False (boolean)
'''

x=True #True y False son palabras reservadas del lenguaje
print(type(x))

autor='Oscar'
print(type(autor))
carro="This is Andrew's car"
modelo=' 1999'
print(carro + modelo) #el simbolo + permite conectar textos en Pyhton


'''
TIPOS DE ESTRUCTURAS DE DATOS Y METODOS
1. Conjuntos +
2. Tuplas ++
3. Listas +++
4. DIccionarios +++
'''

#Uso de conjuntos
'''
Los sets o conjuntos son estructuras especiales que nos ayudan a almacenar un grupo de elementos.
CUando el orden de los elementos no es relevante podemos utilizar sets de Python.

como se define: {, , , ,}
<class 'set'>
'''

#set1={"a", "b", "c", "d"}
#print(type(set1))

#set2=("e", "f", "g")

#metodos para el tratamiento de conjuntos
#set1.union()
#Union de conjunto
#print(set1.union(set2))

#set3=("a", "b", "c", "c", "d", "d")
#print(set3)
#set4=set3.union(set1)
#print(set4)

#Interseccion de conjuntos
#set5=("f", "w", "a", "b")
#print(set5.intersection(set1))

#set5.remove("w")
#print(set5)

#set4.add("z")


#set6=("Oscar", 5, True)
#set7=("Oscar", 5, True, "daniel")
#print(set6.issubset(set7)) #False
#print(set7.issuperset(set6)) #True

#print(set6.issubset(set7)) #True
#print(set7.issubset(set6)) #False

#Uso de tuplas
'''
como se define: [, , , ,]
<class 'tuple'>
Son estructuras de datos que no permiten muchos metodos
se usan cuando queremos registrar informacion (inmutable)
'''

tupla1=(1, 1, 1, 1, 1, 1, 1, 2, 3, 4)
print(type(tupla1))

conteo=tupla1.count(8)
print(conteo)

#index
indice=tupla1.index(3)
print(indice)

'''
PYTHON ES UN LENGUAJE INDEXADO EN BASE 0
El indice 0, en otras palabras, es el primer elemento de la lista
indice <==> posicion
'''

'''
Uso de listas
Las listas en Python son estructuras de datos que almacenan
elementos de manera ordenada y mutable.
Son un tipo de dato nativo del lenguaje
como se define: [, , , ,]
si permiten valores duplicados
<class 'list'>
puede contener cualquier tipo de dato,
numeros, letras, otras listas, etc.
'''

lista1=[8,9,7,5,4,10]
print(type(lista1))

lista2=["jhon", "alejandro", "lewin",],["isabel", "juan", "daniel"]
print(type(lista2)) #class 'list'

#metodos para el tratamiento de listas
#count
print(lista1.count(14)) #0
#reverse
print(lista1.reverse()) #investigar

