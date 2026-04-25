# Luis Marrero
# 801-18-7010
# CCOM 3030-001

# Trabajo de clase: Costo Shipping

# Una compañía de correos cobra por enviar un paquete de acuerdo al peso del paquete en libras.

# La siguiente tabla recoge el costo por libra de cada paquete de acuerdo a su peso.
# Peso del paquete (libras) 	Costo por libra
# libras < 2                         $1.50
# 2 <= libras < 6                    $3.00
# 6 <= libras < 10                   $4.00
# libras >= 10                       $4.75

# Escriba un programa en Python que… Solicite al usuario que ingrese el peso en libras del paquete a enviar.
# Calcule el costo del envío del paquete.
# Despliegue:
# Un nombre ficticio para la empresa
# El peso del paquete en libras
# El costo del envío

# nombre de la empresa
company = "FedEx"

intro = f"Bienvenidos a {company}"
print(intro)
print("-" * len(intro), end="\n\n")

weight = float(input("Entre el peso del paquete en libras: "))

if weight < 2:
    cost_per_pound = 1.50
elif weight < 6:
    cost_per_pound = 3.00
elif weight < 10:
    cost_per_pound = 4.00
else:
    cost_per_pound = 4.75

total_cost = cost_per_pound * weight

print(f"El peso del paquete es: {weight} libras")

print(f"El costo del envío es: ${total_cost:.2f}")

print()
print("Fin del programa")
