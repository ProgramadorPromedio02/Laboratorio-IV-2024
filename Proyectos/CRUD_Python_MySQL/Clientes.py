from Conexion import *

class CClientes:
    def mostrarClientes():
      try:
        cone = CConexion.ConexionBasedeDatos()
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM Usuarios;")
        miResultado = cursor.fetchall()
        cone.commit()
        cone.close()
        return miResultado

      except mysql.connector.Error as error:
        print(f"Error al mostrar los datos: {error}.")

    def ingresarClientes(Nombres, Apellidos, Sexo):
      try:
        cone = CConexion.ConexionBasedeDatos()
        cursor = cone.cursor()
        sql = "INSERT INTO Usuarios VALUES (null, %s, %s, %s);"
        valores = (Nombres, Apellidos, Sexo)
        cursor.execute(sql, valores)
        cone.commit()
        print(cursor.rowcount, "Registro Ingresado")
        cone.close()

      except mysql.connector.Error as error:
        print(f"Error de ingreso de datos: {error}.")

    def modificarClientes(IdUsuario, Nombres, Apellidos, Sexo):
      try:
        cone = CConexion.ConexionBasedeDatos()
        cursor = cone.cursor()
        sql = "UPDATE Usuarios SET Usuarios.Nombres = %s, Usuarios.Apellidos = %s, Usuarios.Sexo = %s WHERE Usuarios.Id = %s;"
        valores = (Nombres, Apellidos, Sexo, IdUsuario)
        cursor.execute(sql, valores)
        cone.commit()
        print(cursor.rowcount, "Registro Actualizado")
        cone.close()

      except mysql.connector.Error as error:
        print(f"Error de actualización de datos: {error}.")

    def eliminarClientes(IdUsuario):
      try:
        cone = CConexion.ConexionBasedeDatos()
        cursor = cone.cursor()
        sql = "DELETE from Usuarios WHERE Usuarios.Id = %s;"
        valores = (IdUsuario,)
        cursor.execute(sql, valores)
        cone.commit()
        print(cursor.rowcount, "Registro Eliminado")
        cone.close()

      except mysql.connector.Error as error:
        print(f"Error de eliminación de datos: {error}.")
