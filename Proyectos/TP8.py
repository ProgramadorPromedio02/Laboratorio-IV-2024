# TP8
print('TP8\n')

## 1.
print('1.')
my_dictonary = {'titulo': 'Base de Datos - El camino de los datos a la información', 'autor': 'Patricio Araneda', 'anio': 2022}
print(my_dictonary['anio']) # 2022
print()

## 2.
print('2.')
my_student = {'nombre': 'Juan', 'edad': 16}
print(f'Datos del estudiante: {my_student}')
my_student['grado'] = '5to 5ta'
print(f'Nueva clave-valor: {my_student}\n')

## 3.
print('3.')
my_product = {'nombre': 'Laptop', 'precio': 800}
print(f'Datos del producto: {my_product}')
my_product['precio'] = 1200
print(f'Precio modificado: {my_product}\n')

## 4.
print('4.')
my_person = {'nombre': 'María', 'edad': 30, 'direccion': 'Calle False 123'}
print(f'Mi persona: {my_person}')
del my_person['direccion']
print(f'Clave "direccion" eliminado: {my_person}\n')

## 5.
print('5.')
my_city = {'nombre': 'Buenos Aires', 'poblacion': 230000}
var = input('Ingrese "nombre" para la variable:\n')
var.lower()

if var in my_city:
  print(f'Nombre de la ciudad existente: {my_city["nombre"]}\n')
else:
  print('❌Error❌: ejecute de nuevo el programa y vuelva a intentarlo\n')

## 6.
print('6.')
my_animal = {'especie': 'perro', 'edad': 15}
var = input('Ingrese "edad" para la variable:\n')
var.lower()

if my_animal.get(var):
  print(f'Edad del animal existente: {my_animal["edad"]}')
else:
  print('❌Error❌: ejecute de nuevo el programa y vuelva a intentarlo\n')

## 7.
print('7.')
my_car = {'marca': 'Toyota', 'modelo': 'Rav4'}
print(f'Datos del coche: {my_car}')
my_car.update({'anio': 1966})
my_car.update({'modelo': 'Corolla'})
print(f'Agregado clave "anio" y valor "1966" y modelo modificado: {my_car}')

## 8.
print('8.')
my_product = {'nombre': 'Oreo', 'precio': 800, 'stock': 1200}
print(f'Datos del producto: {my_product}')
my_product.pop('stock')
print(f'Clave "stock" eliminada: {my_product}')
