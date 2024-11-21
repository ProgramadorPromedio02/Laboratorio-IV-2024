# TP5
print('TP5\n')
## Problema 1: Verificar Edad para Votación
print('Problema 1: Verificar Edad para Votación')
edad = int(input('Ingrese su edad para votar:\n'))

if edad >= 18:
  print('Puedes votar.')
else:
  print('No puedes votar.')

## Problema 2: Calcular Descuento en una Tienda
print('Problema 2: Calcular Descuento en una Tienda')
monto = int(input('Ingrese un precio para el monto:\n'))

if monto >= 1000:
  # monto /= 100
  # monto *= 10
  monto *= 0.10
  print(f'Tu monto es del 10%, mayor o igual a 1000 pesos: {monto}')
else:
  print(f'Tu monto es: {monto}')

## Problema 3: Determinar el Tipo de Triángulo
print('Problema 3: Determinar el Tipo de Trinángulo')
lado1 = int(input('Ingrese un valor numerico para el lado 1:\n'))
lado2 = int(input('Ingrese un valor numerico para el lado 2:\n'))
lado3 = int(input('Ingrese un valor numerico para el lado 3:\n'))

if lado1 == lado2 and lado2 == lado3:
  print(f'Es un Triángulo Equilátero.\n• Lado 1: {lado1}\n• Lado 2: {lado2}\n• Lado 3: {lado3}\n')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
  print(f'Es un Triángulo Isósceles.\n• Lado 1: {lado1}\n• Lado 2: {lado2}\n• Lado 3: {lado3}\n')
else:
  print(f'Es un Triángulo Escaleno.\n• Lado 1: {lado1}\n• Lado 2: {lado2}\n• Lado 3: {lado3}\n')

## Problema 4: Clasificación del IMC
print('Problema 4: Clasificación del IMC')
peso = float(input('Calcula tu peso:\n'))
altura = float(input('Calcula tu altura:\n'))
imc = peso / (altura ** 2)

if imc < 18.5:
  print('Bajo peso\n')
elif imc >= 18.5 and imc < 24.9:
  print('Normal\n')
elif imc >= 25 and imc < 29.9:
  print('Sobrepeso\n')
else:
  print('Obesidad\n')

## Problema 5: Determinar el Año Bisiesto
print('Problema 5: Determinar el Año Bisiesto')
anio = int(input('Introduce un año:\n'))

if anio % 4 == 0:
  if anio % 100 != 0 or anio % 400 == 0:
    print(f'{anio} es un año bisiesto.')
  else:
    print(f'{anio} no es un año bisiesto.')
else:
  print(f'{anio} no es un año bisiesto.')