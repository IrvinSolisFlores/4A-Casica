import tkinter as tk
from tkinter import messagebox, ttk
from productos_controller import (
    ver_productos,
    crear_productos,
    obtener_producto_por_id,
    actualizar_producto_por_id,
    eliminar_producto_por_id
)

class DashboardProductos:
    def __init__(self, usuario):
        self.usuario = usuario
        self.root = tk.Tk()
        self.root.title(f"Bienvenido {usuario}")
        self.root.geometry("800x500")
        self.root.resizable(True, True)
        self.crear_elementos()
        self.root.mainloop()
        
    def crear_elementos(self):
        tk.Label(
            self.root, 
            text=f"Hola {self.usuario}", 
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        tk.Button(
            self.root, text="Ver Productos", width=30,
            command=self.ver_productos
        ).pack(pady=5)

        tk.Button(
            self.root, text="Agregar Producto", width=30,
            command=self.agregar_producto
        ).pack(pady=5)

        tk.Button(
            self.root, text="Actualizar Producto", width=30,
            command=self.actualizar_producto
        ).pack(pady=5)

        tk.Button(
            self.root, text="Eliminar Producto", width=30,
            command=self.eliminar_producto
        ).pack(pady=5)
        
        tk.Button(
            self.root, text="Cerrar sesión", width=30,
            command=self.cerrar_sesion
        ).pack(pady=5)

        # Tabla de productos
        self.tree = ttk.Treeview(
            self.root,
            columns=("ID", "Nombre", "Descripcion", "Precio", "Status", "Marca", "Proveedor"),
            show="headings", height=10
        )
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        self.tree.pack(pady=10, padx=10, fill="both", expand=True)

    # === Métodos ===
    def ver_productos(self):
        productos = ver_productos()
        for row in self.tree.get_children():
            self.tree.delete(row)
        for p in productos:
            self.tree.insert("", tk.END, iid=p[0], values=p)

    def agregar_producto(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Producto")
        ventana.geometry("400x450")

        # Diccionario para guardar los Entry widgets
        entries = {}

        campos = [
            ("nombre", "Nombre del Producto"),
            ("descripcion", "Descripción"),
            ("precio", "Precio"),
            ("status", "Status"),
            ("marca", "Marca"),
            ("proveedor", "Proveedor")
        ]

        for campo, texto in campos:
            tk.Label(ventana, text=texto).pack(pady=5)
            entry = tk.Entry(ventana)
            entry.pack(pady=5)
            entries[campo] = entry

        def guardar():
            nombre = entries["nombre"].get().strip()
            descripcion = entries["descripcion"].get().strip()
            precio = entries["precio"].get().strip()
            status = entries["status"].get().strip()
            marca = entries["marca"].get().strip()
            proveedor = entries["proveedor"].get().strip()

            if not (nombre and descripcion and precio):
                messagebox.showwarning("Campos vacíos", "Nombre, descripción y precio son obligatorios.")
                return
            
            if crear_productos(nombre, descripcion, precio, status, marca, proveedor):
                messagebox.showinfo("Éxito", f"Producto '{nombre}' creado correctamente.")
                self.ver_productos()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo crear el producto.")
        
        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=20)

    def actualizar_producto(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Sin selección", "Seleccione un producto para editar.")
            return

        id_producto = int(selected_item)
        datos = obtener_producto_por_id(id_producto)
        if not datos:
            messagebox.showerror("Error", "No se pudo obtener la información del producto.")
            return

        nombre_actual, descripcion_actual, precio_actual, status_actual, marca_actual, proveedor_actual = datos

        ventana = tk.Toplevel(self.root)
        ventana.title(f"Editar Producto (ID: {id_producto})")
        ventana.geometry("400x450")

        entries = {}
        campos = [
            ("nombre", "Nombre del Producto", nombre_actual),
            ("descripcion", "Descripción", descripcion_actual),
            ("precio", "Precio", precio_actual),
            ("status", "Status", status_actual),
            ("marca", "Marca", marca_actual),
            ("proveedor", "Proveedor", proveedor_actual),
        ]

        for campo, texto, valor in campos:
            tk.Label(ventana, text=texto).pack(pady=5)
            entry = tk.Entry(ventana)
            entry.insert(0, str(valor))
            entry.pack(pady=5)
            entries[campo] = entry

        def guardar_cambios():
            nombre = entries["nombre"].get().strip()
            descripcion = entries["descripcion"].get().strip()
            precio = entries["precio"].get().strip()
            status = entries["status"].get().strip()
            marca = entries["marca"].get().strip()
            proveedor = entries["proveedor"].get().strip()

            if actualizar_producto_por_id(id_producto, nombre, descripcion, precio, status, marca, proveedor):
                messagebox.showinfo("Éxito", f"Producto '{nombre}' actualizado correctamente.")
                self.ver_productos()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el producto.")

        tk.Button(ventana, text="Guardar cambios", command=guardar_cambios).pack(pady=20)

    def eliminar_producto(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Sin selección", "Seleccione un producto para eliminar.")
            return

        id_producto = int(selected_item)
        nombre = self.tree.item(selected_item)["values"][1]

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Desea eliminar el producto '{nombre}' (ID: {id_producto})?"
        )

        if confirmar:
            if eliminar_producto_por_id(id_producto):
                messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
                self.ver_productos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto.")

    def cerrar_sesion(self):
        if messagebox.askyesno("Cerrar Sesión", "¿Seguro que desea cerrar sesión?"):
            self.root.destroy()

if __name__ == "__main__":
    DashboardProductos("Irvin")
