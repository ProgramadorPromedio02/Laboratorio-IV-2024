import mysql.connector

class CConexion:
  def ConexionBasedeDatos():
    try:
      conexion = mysql.connector.connect(user='root', password='Adm1n!Str@t0r#2024',
                                        host='127.0.0.1',
                                        database='ClientesDB',
                                        port='3306')

      print("Conexión Correcta")
      return conexion

    except mysql.connector.Error as error:
      print(f"Error al conectarte a la base de datos: {error}.")
      return conexion

  ConexionBasedeDatos()