# Promedio con centinela

suma = 0
cantidad = 0
nota = float(input("Ingresa otra nota, o ingresa '-1' si quieres salir: "))

while nota != -1:
    suma += nota
    cantidad += 1
    nota = float(input("Ingresa otra nota, o ingresa '-1' si quieres salir: "))

if cantidad > 0:
    print("Promedio: ", suma/cantidad)
else:
    print("No ingresaste notas")
