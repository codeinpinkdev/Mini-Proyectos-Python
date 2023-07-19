import random

while True:
    print("¡Juguemos a ... Piedra, papel o tijera!")
    print("1) Piedra\n2) Papel\n3) Tijera")
    
    # Ingreso de opción para el usuario
    user_option = int(input("¿Cuál es tu opción? (Ingresa el número correspondiente): "))
    
    option_tuple = (1, 2, 3)
    
    # Ingreso de opción de la computadora (número aleatorio del 1 al 3)
    computer_option = random.choice(option_tuple)
    
    # Computadora saca esta opción.
    print("La computadora saca:", computer_option)
    
    # Evaluamos con if
    if user_option == computer_option:
        print("¡Empate!, wow, empataste a la computadora")
    elif user_option == 1 and computer_option == 2:
        print("¡Pierdes!... Computadora saca papel, papel envuelve piedra.")
    elif user_option == 1 and computer_option == 3:
        print("¡Ganas!... Computadora sacó tijera, piedra rompe tijera.")
    elif user_option == 2 and computer_option == 1:
        print("¡Ganas!... Computadora sacó piedra, papel envuelve a la piedra.")
    elif user_option == 2 and computer_option == 3:
        print("¡Pierdes!... Computadora 1sacó tijera, tijera rompe papel.")
    elif user_option == 3 and computer_option == 1:
        print("¡Pierdes!... Computadora sacó piedra, piedra rompe tijera.")
    elif user_option == 3 and computer_option == 2:
        print("¡Ganas!... Computadora sacó papel, tijera rompe papel.")
    else:
        print("Elige una opción válida, ¡inténtalo de nuevo!")
    
    play_again = input("¿Quieres jugar de nuevo? (s/n): ")
    
    if play_again.lower() != 's':
        print("Gracias por jugar. ¡Hasta luego!")
        break
