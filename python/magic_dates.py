# Luis Marrero
# 801-18-7010
# CCOM 3030-001

# Determinar si una fecha es un magic date
# La fecha 10 de junio de 1960 es una fecha especial ya que si la escribimos en el formato 10/06/60, cuando multiplicamos el día por el mes, 
# obtenemos el año. A esto le llamamos un Magic Date.
# 10/06/60 -> 10 * 6 = 60
# Otro ejemplo:
# 02/02/04 -> 2 * 2 = 4

# Escriba un programa que le pida al usuario el día, el mes y el año (en forma numérica). El programa debe…
# Verificar si la fecha es un Magic Date,
# Si lo es, debe desplegar que la fecha es un Magic Date,
# Si no lo es, debe desplegar que la fecha no es un Magic Date.

# Bienvenida

intro = "Programa para determinar si una fecha es un magic date"

print()
print(intro)
print("-" * len(intro), end="\n\n")

day = int(input("Entre el día (en forma numérica 1-31): "))
month = int(input("Entre el mes (en forma numérica 1-12): "))
year = int(input("Entre el año (en forma numérica 00-99): "))

print()
print(f"La fecha que usted ha ingresado es: {day}/{month}/{year}")
print(f"El producto del día {day} y el mes {month} es: {day * month}")

if day * month == year:
    print("La fecha es un Magic Date")
else:
    print("La fecha no es un Magic Date")

print()
print("Fin del programa")
