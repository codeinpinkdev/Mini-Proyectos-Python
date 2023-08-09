import utils as u

data = [
    {
       'Country': 'México',
       'Population': 2342
    },
    {
       'Country': 'Colombia',
       'Population': 6546
    },
    {
       'Country': 'Ecuador',
       'Population': 5697
    }
  ]

def run():
  keys, values = u.get_population()
  #print(keys, values)
  
  opcion = input("¿De qué pais quieres saber la población? ")
  resultado = u.population_by_country(data, opcion)
  print(resultado)

if __name__ == '__main__':
  run()