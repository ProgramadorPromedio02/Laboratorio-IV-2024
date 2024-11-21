# TP4
print('TP4\n')
## 1. Operaciones Aritméticas
print('1. Operaciones Aritméticas\n')
### a.
print('a.')
num1 = int(input('Ingresa un número:\n'))
num2 = int(input('Ingresa otro número:\n'))
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2
print(f'Número 1: {num1}\nNúmero 2: {num2}\nSuma: {suma}\nResta: {resta}\nMultiplicación: {multi}\nDivisión: {div}\n')
### b.
print('b.')
num1 = int(input('Ingresa un número:\n'))
num2 = int(input('Ingresa otro número:\n'))
divInt = num1 // num2
module = num1 % num2
print(f'Número 1: {num1}\nNúmero 2: {num2}\nDivisión Entera: {divInt}\nMódulo: {module}\n')
### c.
print('c.')
num1 = int(input('Ingrese un número para la base:\n'))
num2 = int(input('Ingrese un número para el exponente:\n'))
potencia = num1 ** num2
print(f'Número 1: {num1}\nNúmero 2: {num2}\nPotencia: {potencia}\n')
## 2. Operaciones Lógicas
print('2. Operaciones Lógicas\n')
### a.
print('a.')
input1 = input('Ingrese un valor booleano("True" o "False"):\n')
input2 = input('Ingrese otro valor booleano("True" o "False"):\n')
input1 = input1.capitalize()
input2 = input2.capitalize()
bool1 = bool(input1 == 'True')
bool2 = bool(input2 == 'True')
print(f'Booleano 1: {bool1}\nBooleano 2: {bool2}\nAND: {bool1 and bool2}\nOR: {bool1 or bool2}\nNOT Booleano 1: {not bool1}\nNOT Booleano 2: {not bool2}\n')

## 3. Asignaciones
print('3. Asignaciones\n')
### a.
print('a.')
var = int(input('Introduzca un valor numerico para la variable:\n'))
op = int(input('Introduzca un valor numerico para las operaciones:\n'))
var += op
print(f'Suma: {var}')
var -= op
print(f'Resta: {var}')
var *= op
print(f'Multiplicación: {var}')
var /= op
print(f'División: {var}')
var **= op
print(f'Exponente: {var}')
var //= op
print(f'División entera: {var}')
var %= op
print(f'Módulo: {var}\n')

## 4. Operaciones Relacionales
print(f'Operaciones Relacionales\n')
### a.
print('a.')
num1 = int(input('Ingrese un número para el número 1:\n'))
num2 = int(input('Ingrese un número para el número 2:\n'))
print(f'Número 1: {num1}\nNúmero 2: {num2}\n• {num1} mayor que(>) {num2}: {num1 > num2}\n• {num1} menor que(<) {num2}: {num1 < num2}\n• {num1} igual (==) a {num2}: {num1 == num2}\n')
### b.
print('b.')
num1 = int(input('Ingrese un número para el número 1:\n'))
num2 = int(input('Ingrese un número para el número 2:\n'))
print(f'Número 1: {num1}\nNúmero 2: {num2}\n• {num1} mayor igual que(>=) {num2}: {num1 >= num2}\n• {num1} menor que(<=) {num2}: {num1 <= num2}\n• {num1} no igual(!=) a {num2}: {num1 != num2}\n')