import matplotlib.pyplot as plt

def generate_chart_barras(labels,values):
  
  

  #fig=figura, ax=coordendas {son variables de matplotlib}
  fig, ax = plt.subplots()
  #Quiero generar un gráfico de barras
  ax.bar(labels,values)
  plt.show()

def generate_chart_pastel(labels,values):
  fig, ax = plt.subplots()
   #Quiero generar un gráfico de pastel, el label se asigna a label.
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

#Ejecutar el programa como un script desde main

if __name__ == '__main__':
  labels=['a','b','c']
  values=['20','34','66']
  #generate_chart_barras(labels,values)
  generate_chart_pastel(labels,values)
