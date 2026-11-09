# Adivina el número

numsecret = 7

numero = int(input("Adivina el número secreto del 1 al 10: "))
while numero != numsecret:
    if numero < numsecret:
        print("Muy bajo")
    else:
        print("Muy alto")
    numero = int(input("Inténtalo de nuevo:"))

print("¡Acertaste!")
