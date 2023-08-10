import utils
import readcsv
import charts

def run():
  data = readcsv.read_csv('./app/data.csv')
  #Filtro para filtrado por Continente. Descomentar
  #data = list(filter(lambda item : item['Continent'] == 'South America',data))
  #Termina filtro para filtrado por Continente

  #Inicia código para graficar la población del mundo. Descomentar
  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
   #Termina código para graficar la población del mundo.

  #Inicia código para gráficar población de un pais que yo seleccione.
  """
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  """
  #Termina código para gráficar población de un pais que yo seleccione.
if __name__ == '__main__':
  run()