# Menú que se repite

palabra = "" 

while palabra != "Salir":
    palabra = input("Escribe 'Hola' o 'Salir': ")
    if palabra == "Hola":
         print("¡Hola, mucho gusto!")
    elif palabra != "Salir":
         print("Opción no válida")
         
print("Hasta luego")