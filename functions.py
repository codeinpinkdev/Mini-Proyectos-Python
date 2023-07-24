import random

#Funcion que recibe dos parametros y calcula las operaciones básicas con esos números.
def my_print(num_a, num_b):
  print("\nNúmeros:", num_a, "y", num_b)
  print("Suma: ", num_a + num_b)
  print("Resta: ", num_a - num_b)
  print("Multiplicacion: ", num_a * num_b)
  print("División: ", num_a / num_b)
  print("\n")

#Declaro los números
num_a = random.randint(1, 50)
num_b = random.randint(1, 50)
my_print(num_a, num_b)
