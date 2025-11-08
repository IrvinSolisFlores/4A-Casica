from database import crear_conexion

def ver_usuarios():
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        
        query = "SELECT * FROM Usuarios"
        cursor.execute(query)
        
        usuarios = cursor.fetchall()
        cursor.close()
        conexion.close()
        return usuarios
    except Exception as e:
        print(f"Error al obtener usuarios: {e}")
    return []

def crear_usuarios(usuario, password):
    conexion = crear_conexion()
    if not conexion:
        return False  
    
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO Usuarios (Username, password) VALUES (%s, %s)"
        cursor.execute(query, (usuario, password))
        conexion.commit()
        cursor.close()
        return True
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return False
    
def obtener_usuario_por_id(id_usuario):
    """
    Obtiene el Username y Password de un usuario específico usando su ID.
    Lo necesitamos para rellenar el formulario de edición.
    """
    conexion = crear_conexion()
    if not conexion: 
        return None
    try:
        cursor = conexion.cursor()
        # Nota: Seleccionamos la contraseña aquí solo para el formulario de edición
        query = "SELECT Username, password FROM Usuarios WHERE ID = %s"
        cursor.execute(query, (id_usuario,))
        usuario = cursor.fetchone() # Devuelve una tupla (username, password)
        cursor.close()
        return usuario
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return None

def actualizar_usuario_por_id(id_usuario, nuevo_username, nueva_password):
    """
    Actualiza el Username y la Password de un usuario buscando por su ID.
    """
    conexion = crear_conexion()
    if not conexion: 
        return False
    
    try:
        cursor = conexion.cursor()
        
        # --- ESTA ES LA CONSULTA CORRECTA ---
        query = "UPDATE Usuarios SET Username = %s, password = %s WHERE ID = %s"
        
        # El orden de la tupla debe coincidir: (nuevo_username, nueva_password, id_del_usuario)
        cursor.execute(query, (nuevo_username, nueva_password, id_usuario))
        # ------------------------------------
        
        conexion.commit()
        
        filas_afectadas = cursor.rowcount
        cursor.close()
        
        return filas_afectadas > 0 # Devuelve True si se actualizó (filas_afectadas > 0)
        
    except Exception as e:
        print(f"Error al actualizar usuario por ID: {e}")
        return False
def eliminar_usuario_por_id(id_usuario):
    """
    Elimina un usuario de la base de datos usando su ID.
    """
    conexion = crear_conexion()
    if not conexion: 
        return False
    
    try:
        cursor = conexion.cursor()
        
        # --- Consulta SQL para eliminar ---
        query = "DELETE FROM Usuarios WHERE ID = %s"
        
        cursor.execute(query, (id_usuario,))
        # ---------------------------------
        
        conexion.commit()
        
        filas_afectadas = cursor.rowcount
        cursor.close()
        
        # Devuelve True solo si se eliminó 1 fila
        return filas_afectadas > 0 
        
    except Exception as e:
        print(f"Error al eliminar usuario: {e}")
        return False