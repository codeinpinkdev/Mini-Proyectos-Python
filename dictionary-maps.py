items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

prices = list(map(lambda item: item['price'], items))
print(items)
print(prices)

def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items = list(map(add_taxes, items))
print(new_items)
print(items)

"""
2. Dada una lista de diccionarios con claves "nombre" y "edad", aplicar un incremento de 5 años a la edad de cada persona.
"""

lista = [ {
            'nombre' : 'Patricia',
            'edad': 20
          },
          { 
            'nombre' : 'Jesus',
            'edad': 32
          },
         { 
            'nombre' : 'Guadalupe',
            'edad': 28
          },
         { 
            'nombre' : 'Jose',
            'edad': 15
          }
        ]


resultado = list(map(lambda persona: {**persona, **{'edad': persona['edad'] + 5}}, lista))
print(resultado)

"""
3. Dada una lista de diccionarios con claves "producto" y "precio", aplicar un descuento del 10% al precio de cada producto.
"""

lista = [ {
            'producto' : 'Laptop',
            'precio': 6500
          },
          { 
            'producto' : 'Mouse',
            'precio': 300
          },
         { 
            'producto' : 'Teclado',
            'precio': 500
          },
         { 
            'producto' : 'Monitor',
            'precio': 800
          }
        ]


resultado = list(map(lambda producto: {**producto, 
  **{'precio':producto['precio']*.90}}, lista))
print(resultado)

"""
4. Dada una lista de diccionarios con claves "nombre" y "sueldo", aplicar un incremento salarial del 15% a cada empleado.
"""

lista = [ {
            'nombre' : 'rodrigo',
            'sueldo': 10000
          },
          { 
            'nombre' : 'juana',
            'sueldo': 3000
          },
         { 
            'nombre' : 'romel',
            'sueldo': 1500
          },
         { 
            'nombre' : 'bertha',
            'sueldo': 30000
          }
        ]


resultado = list(map(lambda sueldo: {**sueldo,**{'sueldo':sueldo['sueldo']*1.15}}, lista))
print(resultado)
