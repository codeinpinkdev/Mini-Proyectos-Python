def get_population():
  keys = ['mex','bol']
  values = ['400', '399']
  return keys, values

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country']==country, data))
  return result

