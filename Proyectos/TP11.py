# TP11
print('TP11\n')

# 1.
print('1.')
def suma(a, b):
  print(a + b)

suma(2, 4) # 6
print()

# 2.
print('2.')
def factorial(num):
  if num < 0:
    return "El factorial no está definido para números negativos."
  elif num == 0 or num == 1:  
    return 1

  result = 1
  for i in range(1, num + 1):
    result *= i
  return result

print(factorial(4)) # 24
print()

# 3.
print('3.')
def es_par(num):
  if num % 2 == 0:
    return f'El número es par: {num}\n'
  else:
    return f'El número es impar: {num}\n'

num = int(input('Ingresa un número que sea par: '))
print(es_par(num))

# 4.
print('4.')
def contar_vocales(phrase):
  vowels_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
  count_vocals = 0
  phrase = phrase.lower()
  for i in phrase:
    if i in vowels_count:  
      vowels_count[i] += 1
      count_vocals += 1
  print(f'La cantidad de vocales en esta cadena de texto es: {count_vocals}.\n')

string = input('Ingresa una frase: ')
print(string)
contar_vocales(string)

# 5.
print('5.')
def invertir_cadena(str):
    str = list(str)  # Convertir la cadena de texto en una lista.
    str.reverse()   # Invertir el orden de los elemento de la lista.
    str = ''.join(str)  # Convertir la lista de vuelta a una cadena de texto
    print(f'Cadena invertida: {str}\n')

string = input('Ingresa una frase: ')
print(f'Cadena original: {string}')
invertir_cadena(string)

# 6.
print('6.')
def maximo(lista):
  lista = [int(i) for i in lista]
  numero_maximo = max(lista)
  print(f'El número más grande es: {numero_maximo}\n')

mi_lista = []
limite = {1, 2, 3, 4, 5}

for i in limite:
  mi_lista.append(input('Ingrese 5 números para saber el número más grande: '))
  print(f'{i}/5')

maximo(mi_lista)

# 7.
print('7.')
def calcular_media(lista):
  lista = [int(i) for i in lista]
  promedio = sum(lista) / len(lista)
  
  print(f'El promedio de todos los números es: {promedio}\n')

mi_lista = []
limite = {1, 2, 3, 4, 5}

for i in limite:
  mi_lista.append(input('Ingrese 5 números para calcular el promedio de todos: '))
  print(f'{i}/5')

calcular_media(mi_lista)

# 8.
print('8.')

def contar_palabras(frase):
  words_per_phrase = []
  words = frase.split()
  count_words = len(words)
  words_per_phrase.append(count_words)
  
  if count_words == 1:
    print(f'Tu frase: "{frase}" tiene {count_words} palabra.\n')
  else:
    print(f'Tu frase: "{frase}" tiene {count_words} palabras.\n')


string = input('Ingrese una frase, y de diré la cantidad de palabras en tu cadena.\n')
contar_palabras(string)

# 9.
print('9.')

def numeros_pares(lista_num):
  pares = []
  for num in lista_num:
    if num % 2 == 0:
      pares.append(num)
  print(f'{pares}\n')

mi_lista = [1, 2, 3, 4, 5, 6, 8, 9, 10]
numeros_pares(mi_lista)

# 10.
print('10.')

def elementos_unicos(lista):
  conjunto = set(lista)
  print(conjunto)

mi_lista = []
limite = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

for i in limite:
  mi_lista.append(input('Ingrese 10 elementos de una lista, pero si son repetidos, va a tomarlo como único: \n'))
  print(f'{i}/10')

elementos_unicos(mi_lista)
