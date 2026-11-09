# Suma hasta N

N = int(input("Hasta qué numero quieres sumar? "))
suma = 0

for i in range(1, N + 1):
    suma += i    

print("La suma es: ", suma)