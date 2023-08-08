import functools

"""
1. Dada una lista de diccionarios con claves "producto" y "cantidad", calcular el total de la cantidad de productos.
"""

lista = [ {
            'producto' : 'cajas',
            'cantidad': 50
          },
          { 
            'producto' : 'lapices',
            'cantidad': 32
          },
         { 
            'producto' : 'cuadernos',
            'cantidad': 12
          },
         { 
            'producto' : 'pincel',
            'cantidad': 3
          }
        ]


resultado = functools.reduce(lambda counter, cantidad: counter+cantidad['cantidad'], lista, 0)
print(resultado)

import functools

"""
2. Dada una lista de diccionarios con claves "nombre" y "puntuacion", calcular el promedio de puntuaciones.
"""

lista = [ {
            'nombre' : 'juan',
            'puntuacion': 9.5
          },
          { 
            'nombre' : 'lau',
            'puntuacion': 6.4
          },
         { 
            'nombre' : 'miguel',
            'puntuacion': 10
          },
         { 
            'nombre' : 'poncho',
            'puntuacion': 8.9
          }
        ]


resultado = functools.reduce(lambda counter, puntuac: counter+puntuac['puntuacion']/4, lista, 0)
print(resultado)
