# TP3
print('TP3\n')
## 2.
print('2.\n')
### a. 
print('a.')
user = input("Introduzca su nombre de usuario:\n")
capitalize = user.capitalize()
print(f'¡Bienvenido {capitalize}!')

### b.
print('b.')
text = input("Introduzca una cadena de texto:\n")
textCharacter = input("Introduzca el carácter a buscar: \n")

user = input("Introduzca su nombre de usuario otra vez:\n")
userCharacter = input("Introduzca el carácter a buscar: \n")

text.capitalize()
user.capitalize()

findCtl1 = text.find(textCharacter)
findCtl2 = user.find(userCharacter)

print(f'Cadena encontrada:\n • {findCtl1}. \n • {findCtl2}.')

### c.
print('c.')
text = input("Introduzca una cadena de texto:\n")
textCharacter = input("Introduzca el carácter a buscar: \n")

user = input("Introduzca su nombre de usuario otra vez:\n")
userCharacter = input("Introduzca el carácter a buscar en su nombre de usuario: \n")

indexCtl1 = text.index(textCharacter)
indexCtl2 = user.index(userCharacter)

print(f'El índice del carácter en la cadena de texto y en tu nombre de usuario es:\n • {indexCtl1}. \n • {indexCtl2}.')

### d.
print('d.')
text = input('Introduzca letras o números:\n')
alphaNum = text.isalnum()
print(alphaNum)

### e.
print('e.')
text = input('Introduzca letras:\n')
alpha = text.isalpha()
print(alpha)

### f.
print('f.')
text = input('Introduzca números:\n')
decimal = text.isdecimal()
print(decimal)

### g.
print('g.')
text = input('Introduzca digitos:\n')
digit = text.isdigit()
print(digit)

### h.
print('h.')
text = input('Introduzca texto en mínusculas:\n')
lower = text.islower()
print(lower)

### i.
print('i.')
text = input('Introduzca texto en mayúsculas:\n')
upper = text.isupper()
print(upper)

### j.
print('j.')
text = input('Introduzca su nombre de usuario:\n')
lower = text.lower()
upper = text.upper()
print(f' Texto en mínusculas: {lower}.\n Texto en mayúsculas: {upper}.')