from database import crear_conexion

def ver_productos():
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return productos
    except Exception as e:
        print(f"Error al obtener productos: {e}")
        return []

def crear_productos(nombre, descripcion, precio, status, marca, proveedor):
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        query = """INSERT INTO productos 
                   (nombre_producto, descripcion, precio, status, marca, proveedor)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (nombre, descripcion, precio, status, marca, proveedor))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al crear producto: {e}")
        return False

def obtener_producto_por_id(id_producto):
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        query = """SELECT nombre_producto, descripcion, precio, status, marca, proveedor 
                   FROM productos WHERE id_producto = %s"""
        cursor.execute(query, (id_producto,))
        producto = cursor.fetchone()
        cursor.close()
        conexion.close()
        return producto
    except Exception as e:
        print(f"Error al obtener producto: {e}")
        return None

def actualizar_producto_por_id(id_producto, nombre, descripcion, precio, status, marca, proveedor):
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        query = """UPDATE productos 
                   SET nombre_producto=%s, descripcion=%s, precio=%s, status=%s, marca=%s, proveedor=%s 
                   WHERE id_producto=%s"""
        cursor.execute(query, (nombre, descripcion, precio, status, marca, proveedor, id_producto))
        conexion.commit()
        filas = cursor.rowcount
        cursor.close()
        conexion.close()
        return filas > 0
    except Exception as e:
        print(f"Error al actualizar producto: {e}")
        return False

def eliminar_producto_por_id(id_producto):
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
        conexion.commit()
        filas = cursor.rowcount
        cursor.close()
        conexion.close()
        return filas > 0
    except Exception as e:
        print(f"Error al eliminar producto: {e}")
        return False
