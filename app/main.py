import utils
import read_csv
import charts


'''
data=[
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Venezuela',
    'Population': 700
  }
]
'''

# 1.Recibe un archivo CSV
# 2.Lo convierte en una lista de diccionarios
# 3.Crea otro diccionario solo con los valores a graficar
# 4.Esto develve labels y values 
# 5.Generar el gráfico

def run():
  # Lee el archivo CSV y devuelve una lista de diccionarios
  data=read_csv.read_csv('./data.csv')
  data=list(filter(lambda item: int(item['Year']) > 1985, data)) # Usando un filtro
  
  #print (data)
  
  # Otra manera
  labels=list(map(lambda x: x['Year'], data))
  values=list(map(lambda x: int(x['Population under the age of 25']), data))
  
  print (labels)
  print('---' * 10)
  print (values)
  charts.generate_bar_chart(labels, values)
  charts.generate_pie_chart(labels, values)
  
  
  # Filtra la lista de diccionarios por el año ingresado por el usuario y lo asigna a la variable como un diccionario
'''
  # Otra manera
  labels, values = utils.young_population(data)
  charts.generate_bar_chart(labels, values)
'''


'''  



  # Si la longitud del diccionario es mayor que cero, significa que se encontraron resultados
  if len(result)>0: 
    year=result[0]
    labels, values = utils.population_by_age(year)
    charts.generate_bar_chart(labels, values)


'''
def run2():
  # Lee el archivo CSV y devuelve una lista de diccionarios
  data=read_csv.read_csv('./app/data.csv')
  #print (data)

  year=input('Ingrese el año: ')

  # Filtra la lista de diccionarios por el año ingresado por el usuario y lo asigna a la variable como un diccionario
  result = utils.population_by_year(data, year) 

  # Si la longitud del diccionario es mayor que cero, significa que se encontraron resultados
  if len(result)>0: 
    year=result[0]
    labels, values = utils.population_by_age(year)
    charts.generate_bar_chart(labels, values)


if __name__ == '__main__': # Este if permite que el archivo se pueda ejecutar como un script desde la terminal
  #run2()
  run()
  
















