# Creando mis módulos

def get_population():
  keys = ['col', 'bol']
  values = [300, 400]
  return keys, values

def population_by_age(year_dict):
  population_by_age = {
    '< 1 año': int(year_dict['Population of children under the age of 1']),
    '1 a 4 años': int(year_dict['Population aged 1 to 4 years']),
    '5 a 9 años': int(year_dict['Population aged 5 to 9 years']),
    '10 a 14 años': int(year_dict['Population aged 10 to 14 years']),
    '15 a 19 años': int(year_dict['Population aged 15 to 19 years']),
    '20 a 29 años': int(year_dict['Population aged 20 to 29 years']),
    '30 q 39 años': int(year_dict['Population aged 30 to 39 years']),
    '40 a 49 años': int(year_dict['Population aged 40 to 49 years']),
    '50 a 59 años': int(year_dict['Population aged 50 to 59 years']),
    '60 a 69 años': int(year_dict['Population aged 60 to 69 years']),
    '70 a 79 años': int(year_dict['Population aged 70 to 79 years']),
    '80 a 89 años': int(year_dict['Population aged 80 to 89 years']),
    '90 a 99 años': int(year_dict['Population aged 90 to 99 years']),
    '> 100 años': int(year_dict['Population older than 100 years']),
  }
  
  labels = population_by_age.keys()
  values = population_by_age.values()
  print (population_by_age)
  return labels, values


def young_population(data): # Recibe una lista de diccionarios
  dic3={year['Year']: int(year['Population under the age of 25']) for year in data}
  #print(dic3)
  labels = dic3.keys()
  values = dic3.values()

  return labels, values



A='HOLA'

def population_by_year(data, year):
  result = list(filter(lambda item: item['Year'] == year, data))
  #print (result)
  return result

  
  