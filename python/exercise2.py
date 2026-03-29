# Luis Marrero
# 801-18-7010
# CCOM3030-001

# Calcular ecuación `dividendo = divisor * cociente + residuo`

intro = "Programa para calcular la ecuación: `dividendo = divisor * cociente + residuo`"

print()
print(intro)
print("-" * len(intro), end="\n\n")

# Pedirle al usuario un dividendo y un divisor
# Asumir que el divisor es mayor que cero

dividendo = int(input("Escriba un dividendo: "))
divisor = int(input("Escriba un divisor: "))

# imprimir `dividendo = divisor * cociente + residuo`

print()
print(f"{dividendo} = {divisor} * {dividendo//divisor} + {dividendo%divisor}")
print()
print("Fin del programa")
