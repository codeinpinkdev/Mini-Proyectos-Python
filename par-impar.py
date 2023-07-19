"""
El clásico programa con mod para saber si un número es par o impar.
"""

print(" \n Soy un programita que te dira si tu número es par o impar. \n ¿Estás listo?... \n")
numero = int(input("Escribe tu número: "))

if(numero%2==0):
  print(f"\nEl número {numero} es par, su residuo es 0.")
else:
  print(f"\nEl residuo es decimal, por tanto el número {numero} es impar.")
