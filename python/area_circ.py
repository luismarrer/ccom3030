# Luis Marrero
# 801-18-7010
# CCOM3030-001
 
# Const
PI = 3.14

# Program

intro = "Programa para calcular el área de un círculo"

print()
print(intro)
print("-" * len(intro), end="\n\n")

radio = float(input("Entre el radio del círculo: "))
area_circ = PI * radio ** 2

print()
print("El área de un círculo con", radio, "de radio es:", area_circ, end="\n\n")
print("Fin del programa")
