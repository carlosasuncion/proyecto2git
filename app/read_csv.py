from collections.abc import Iterable
import csv

''' # Esta función lee un archivo CSV e imprime su contenido
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    l = 1
    for row in reader:
      print (l, '***' * 10)
      l+=1
      print(row)
if __name__ == '__main__':
  data = read_csv('./app/data.csv')  
  print('')
  print ('fin')
  '''

# Esta función lee un archivo CSV y lo convierte en una lista de diccionarios
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') # lee el archivo csv
    header = next(reader) # lee la primera fila del archivo csv
    #print (header)
    print ('++' * 10)
    print('')
    
    data = [] # crea una lista vacía
    for row in reader: # lee cada fila del archivo csv
      iterable = zip(header, row) # une las dos listas
      year_dict = {key: value for key, value in iterable} # crea un diccionario a partir de las dos listas
      data.append(year_dict) # agrega el diccionario a la lista
    return data # retorna la lista de diccionarios

if __name__ == '__main__': # ejecuta el código si se está ejecutando el archivo como un script
  data = read_csv('./app/data.csv') # llama a la función read_csv() y asigna el resultado a la variable data
  print(data[1]) # imprime la variable data  
  print('') # imprime un salto de línea
  print ('fin') # imprime el texto "fin"

  
  