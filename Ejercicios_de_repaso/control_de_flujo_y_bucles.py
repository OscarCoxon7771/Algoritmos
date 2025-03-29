'''
If then else son estructuras de control de flujo que permiten ejecutar
diferentes bloques de código según se cumplan o no ciertas condiciones.
'''
x = 100
y = 200

if x > y: #condición
    #bloque de código que se ejecuta si la condición es verdadera
    print("x es mayor que y")
    #bloque de código que se ejecuta si la condición es falsa

elif x == 300: #condición
    print("x es igual a 100")
    #bloque de código que se ejecuta si la condición es falsa    

elif x == 100:
    print("x es igual a 100")
    #bloque de código que se ejecuta si la condición es falsa    
else:
    print("x no es mayor que y")

#elif sirve para evaluar múltiples condiciones

#uso de anidados

usuario = "Oscar"
contrasena = "wasa123"

usuario=input("ingrese su usuario: ")

if usuario == "Oscar": #condición 1 se cumple
    contrasena=input("ingrese su contraseña: ")
    if contrasena == "wasa123": #condición 2 se cumple?
        print("usuario puede acceder")
    else:
        print("contraseña incorrecta")
#else:
    print("usuario incorrecto")


# tambien se puede usar and

usuario = "Oscar"
contrasena = "wasa123"

if usuario == "Oscar" and contrasena == "wasa123":
    print("usuario puede acceder")
else :
    print("usuario o contraseña incorrectos")

#tambien se puede usar or

usuario = "Oscar"
contrasena = "wasa123"


if usuario == "Oscar" or contrasena == "wasa123":
    print("usuario puede acceder")
else :
    print("usuario o contraseña incorrectos")