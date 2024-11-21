# TP12
print('TP12\n')

# 1.
print('1.')
with open('archivos/text.txt', 'r') as texto:
  for linea in texto:
    print(linea)

# 2.
print('2.')
mensaje = "Creando un nuevo fichero y escribiendo un mensaje en él."

with open("archivos/nuevo_archivo.txt", "w+") as archivo:
  archivo.write(mensaje)
  # Mueve el cursor al principio del archivo
  archivo.seek(0)
  for linea in archivo:
    print(linea)

print("El archivo ha sido creado exitosamente.")

# 3.
print('3.')

nuevo_texto = " Añadiendo una nueva linea de texto."

with open("archivos/nuevo_archivo.txt", "a+") as archivo:
  archivo.write(nuevo_texto + "\n")
  # Mueve el cursor al principio del archivo
  archivo.seek(0)
  for linea in archivo:
    print(linea)

print("La línea se ha añadido al final del archivo.")
