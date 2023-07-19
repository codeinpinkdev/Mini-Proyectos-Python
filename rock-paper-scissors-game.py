#Libreria para sacar un numero aleatorio
import random

#Ingreso de opción para el usuario
user_option = int(input("¡Juguemos a ... Piedra, papel o tijera!: \n\n 1) Piedra \n 2) Papel \n 3) Tijera \n\n ¿cuál es tu opción?: "))

#Ingreso de opción de la computadora, le digo que me genere un número aleatorio del 1 al 3 cada que se ejecute el programa.
computer_option = random.randint(1, 3)

#Computadora saca esta opción.
print(computer_option)

#Evaluamos con if

if(user_option==computer_option):
  print("¡Empate!, wow, empataste a la computadora")
elif(user_option==1 and computer_option==2):
  print("\nComputadora saca papel!\n")
  print("¡Pierdes!... Computadora saca papel, papel envuelve piedra.")
elif(user_option==1 and computer_option==3):
  print("\nComputadora saca tijera!\n")
  print("¡Ganas!... Computadora sacó tijera, piedra rompe tijera")
elif(user_option==2 and computer_option==1):
  print("\nComputadora saca piedra!\n")
  print("¡Ganas!... Computadora sacó piedra, papel envuelve a la piedra")
elif(user_option==2 and computer_option==3):
  print("\nComputadora saca tijera!\n")
  print("¡pierdes!... Computadora sacó tijera, tijera rompe papel")
elif(user_option==3 and computer_option==1):
  print("\nComputadora saca piedra!\n")
  print("¡pierdes!... Computadora sacó piedra, piedra rompe tijera")
elif(user_option==3 and computer_option==2):
  print("\nComputadora saca papel!\n")
  print("¡ganas!... Computadora sacó papel, tijera rompe papel")
else:
  print("Escoje una opción valida, ¡intentalo de nuevo!")
