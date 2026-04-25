edad = int(input("Entre su edad: "))

if edad < 12:
    entrada = 4.0
    clasificacion = "niño"
else:
    if 12 <= edad < 65:
        entrada = 7.0
        clasificacion = "adulto"
    else:
        entrada = 5.0
        clasificacion = "senior"

print(f"El costo para una taquilla de {clasificacion} es ${entrada:.2f}.")
