'''
Problema: Crear un diccionario con las calificaciones de 3 estudiantes 
y permitir que el usuario consulte la calificación de uno de ellos.
'''

# Definición del diccionario con las calificaciones
calificaciones = {
    "Osca": 1.2,
    "Lyna": 5.0,
    "Pepe": 3.5
}
# Solicitar al usuario el nombre del estudiante
estudiante = input("Ingrese el nombre del estudiante (Estudiante1, Estudiante2, Estudiante3): ")
# Verificar si el estudiante está en el diccionario
if estudiante in calificaciones:
    # Mostrar la calificación del estudiante
    print(f"La calificación de {estudiante} es: {calificaciones[estudiante]}")
else:
    # Mensaje de error si el estudiante no está en el diccionario
    print("Estudiante no encontrado.")
# Fin del programa
