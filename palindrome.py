'''
Programa al que le introduces una palabra o frase, y te dice si se trata de un palindromo.
'''

palabra = input("Escribe la frase/palabra")
#Si es una frase, uso replace para quitar los espacios.
palabra=palabra.replace(' ','')
#Cambiamos toda la frase a mayuscula.
palabra=palabra.upper()

Palindromo = palabra[::-1]

if(Palindromo==palabra):
  print("Es un Palindromo")
else:
  print("No es palindromo")
