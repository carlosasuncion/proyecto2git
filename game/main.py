# Juego de Piedra, Papel o Tijera

import random

# Función para escoger las opciones
def escoger_opciones():
  options = ('piedra', 'papel', 'tijera')
  
  computer_option = random.choice(options)
  
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()
  while not user_option in options:
    print('Esa opción no es válida')
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()
  
  print('')
  print('User option => ', user_option)
  print('Computer option => ', computer_option)
  print('')
  return user_option, computer_option
# Hasta aquí - Función para escoger las opciones

# Ejecución de la función
user_option, computer_option = escoger_opciones()


if user_option == computer_option:
  print("Empate!")

elif user_option == "piedra":
  if computer_option == "tijera":
    print("piedra gana a tijera")
    print("user ganó!")
  else:
    print("Papel gana a piedra")
    print("computer ganó!")

elif user_option == "papel":
  if computer_option == "piedra":
    print("papel gana a piedra")
    print("user ganó!")
  else:
    print("tijera gana a papel")
    print("computer ganó!")

elif user_option == 'tijera':
  if computer_option == 'papel':
    print("tijera gana a papel")
    print("user ganó!")
  else:
    print("piedra gana a tijera")
    print("computer ganó!")
