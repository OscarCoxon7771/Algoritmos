'''
Problema: Crear un diccionario con algunos productos 
y permitir que el usuario agregue un nuevo producto con su precio.
'''

productos = {
    "Jamoneta": 4000,
    "Huevo frito": 1000,
    "Huevo hervido": 500,
    "Chorizo": 3000,
}
producto= input("Ingrese el nombre del producto: ")
precio= input("Ingrese el precio del producto: ")

print(f"El producto {producto} tiene un precio de {precio}")
productos[producto] = precio
print(productos)

