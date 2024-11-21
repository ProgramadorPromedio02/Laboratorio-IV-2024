# TP10
print('TP10\n')

# 1.
print('1.')
string = 'HelloWorld'
i = 0
while i < len(string):
  print(string[i])
  i += 1
print()

# 2.
print('2.')
string = 'Hello World, what\'s up? Are you okey?'
vowels_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
count_vowels = 0
i = 0

while i < len(string):
  if string[i] in vowels_count.keys(): # if string[i] in vowels_count:
    vowels_count[string[i]] += 1
    count_vowels += 1
  i += 1

print(string)
print(f'El número de vocales es: {count_vowels}\n')

# Imprimir la cantidad de cada vocal en la cadena
# i = 0
# while i < len(vowels_count):
#   vowel, count = list(vowels_count.items())[i]
#   print(f"Vocal '{vowel}' se repite {count} veces.\n")
#   i += 1

# 3.
print('3.')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

while i < len(numbers):
  print(numbers[i])
  i += 1
print()

# 4.
print('4.')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
total = 0

while i < len(numbers):
  total += numbers[i]
  i += 1

print(f'Lista de números:\n{numbers}')
print(f'La suma total de todos los números de la lista es:\n{total}\n')

# 5.
print('5.')
names = ['Gonzalo', 'Matias', 'Lilia', 'Ariel', 'Coffee', 'Negro', 'Manchitas', 'Chiquitin']
i = 0

while i < len(names):
  print(names[i])
  i += 1
print()

# 6.
print('6.')
i = 0
names = ('Gonzalo', 'Matias', 'Lilia', 'Ariel', 'Coffee', 'Negro', 'Manchitas', 'Chiquitin')
name_search = input("Ingrese un nombre para buscar: ")

while i < len(names):
  if names[i] == name_search:
    print(f"Nombre encontrado: {name_search}\n")
    break
  i += 1

if i == len(names):
  print("Nombre no encontrado.\n")

# 7.
print('7.')
i = 0
dic = {'X': 10, 'XX': 20, 'XXX': 30, 'XXXX': 40, 'XXXXX': 50}
keys = list(dic.keys())
while i < len(keys):
  print(keys[i])
  i += 1
print()

# 8.
print('8.')
i = 0
dic = {'X': 10, 'XX': 20, 'XXX': 30, 'XXXX': 40, 'XXXXX': 50}
items = list(dic.items())
while i < len(items):
  print(items[i])
  i += 1
print()
