# Controlador encargado de la logica de autentificacion
#Nos sirve para separar la logica de login para mantener el codigo mas limpio

from database import crear_conexion

def validar_credenciales(usuario, contraseña):
    conexion = crear_conexion()
    if not conexion:
        return False
    cursor = conexion.cursor()
    consulta = "SELECT * FROM Usuarios WHERE Username = %s AND password = %s"
    cursor.execute(consulta, (usuario, contraseña))
    result = cursor.fetchone()
    cursor.close()
    conexion.close()
    return bool(result)