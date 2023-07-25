#Lambda para traes números positivos de una lista.
mi_lista = [18, -3, 5, 0, -1, 12]
lista_nueva = list(filter(lambda x: x > 0, mi_lista))
print(lista_nueva) # [18, 5, 12]

#Lambda para duplicar los valores de un número en la lista.
mi_lista = [1, 2, 3, 4, 5, 6]
lista_nueva = list(map(lambda x: x * 2, mi_lista))
print(lista_nueva)  # [2, 4, 6, 8, 10, 12]

#Ejemplo del curso.
def increment(x):
  return x + 1

#Lambda function.
increment_v2 = lambda x: x + 1

result = increment(10)
print(11)

result = increment_v2(20)
print(result)

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'

text = full_name('patricia', 'velazquez')
print(text)
