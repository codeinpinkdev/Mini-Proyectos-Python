"""
1. Filtrar números pares de una lista de enteros.
"""

lista = [1,2,3,4,5,6,7,8,9,10]
resultado = list(filter(lambda pares:pares%2==0,lista))
print(resultado)

"""
2. Filtrar números primos de una lista de enteros.
"""

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = list(filter(es_primo, lista))
print(resultado)

"""
3. Filtrar palabras que comienzan con una letra específica de una lista de palabras.
"""

lista = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter"]
resultado = list(filter(lambda palabra:(palabra.lower().startswith("m")),lista))
print(resultado)

"""
4. Filtrar nombres de una lista de nombres que tengan más de cierta cantidad de letras.
"""

lista = ["Ana","Juan","Laura","Ramiro","Mario"]
resultado = list(filter(lambda palabra:len(palabra)>5,lista))
print(resultado)

"""
5. Filtrar elementos de una lista de strings que tienen una longitud impar.
"""

lista = ["Ana","Juan","Laura","Ramiro","Mario"]
resultado = list(filter(lambda palabra:len(palabra)%2!=0,lista))
print(resultado)

"""
6. Filtrar los elementos de una lista de diccionarios para obtener aquellos cuyo valor de la clave "edad" sea mayor que 30.
"""

lista = [ {
            'nombre' : 'Patricia',
            'edad': 28 
          },
          { 
            'nombre' : 'Marco',
            'edad': 32
          },
         { 
            'nombre' : 'Laura',
            'edad': 25
          },
         { 
            'nombre' : 'Ramiro',
            'edad': 46
          }
        ]


resultado = list(filter(lambda palabra:palabra['edad']>30,lista))
print(resultado)

"""
7. Filtrar los elementos de una lista de diccionarios para obtener aquellos que contienen una clave "categoria" con un valor específico.
"""

lista = [ {
            'pelicula' : 'saw',
            'genero': 'terror'
          },
          { 
            'pelicula' : 'one day',
            'genero': 'romance'
          },
         { 
            'pelicula' : 'hangover',
            'genero': 'comedia'
          },
         { 
            'pelicula' : 'mi vecino totoro',
            'genero': 'animada'
          }
        ]


resultado = list(filter(lambda pelicula:pelicula['genero']=="terror",lista))
print(resultado)
