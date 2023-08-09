#----- modulo para leer el acrhivo csv --------
import csv

# funcion abrir archivo
def read_csv(path):
  with open(path, 'r') as csvfile:
    #Nota: Reader es Iterable.
    reader = csv.reader(csvfile, delimiter=',')
    cabecera = next(reader)
    data = []
    #print(cabecera)
    #1. Para leer un archivo, primero hay que leerlo linea por linea con un for. 
    for row in reader:
      #2. Se itera la cabecera junto con la fila, en una Tupla.
      iterable = zip(cabecera,row)
      print('***' * 5)
      #print(row)
      #print(list(iterable))
      #3. Crear el diccionario
      country_dicty = {llave: valor for llave, valor in iterable}
      #Agregar el diccionario a una lista vacia creada data para crear una lista de diccionarios
      data.append(country_dicty)
    return data
# correr archivo como script desde la terminal
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data)

