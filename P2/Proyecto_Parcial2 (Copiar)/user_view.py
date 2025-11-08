import tkinter as tk
from user_controller import ver_usuarios, crear_usuarios, obtener_usuario_por_id,actualizar_usuario_por_id, eliminar_usuario_por_id
from tkinter import messagebox
from tkinter import ttk


class DashboardApp:
    def __init__(self, usuario):
        self.usuario = usuario
        self.root = tk.Tk()
        self.root.title(f"Bienvenido {usuario}")
        self.root.geometry("400x300")
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
            self.root, 
            text="Ver Usuarios", 
            width=30, 
            command=self.ver_usuarios
        ).pack(pady=5)

        tk.Button(
            self.root, 
            text="Agregar Usuarios", 
            width=30, 
            command=self.agregar_usuarios
        ).pack(pady=5)

        tk.Button(
            self.root, 
            text="Actualizar Usuarios", 
            width=30, 
            command=self.actualizar_usuarios
        ).pack(pady=5)

        tk.Button(
            self.root, 
            text="Eliminar Usuarios", 
            width=30, 
            command=self.eliminar_usuarios
        ).pack(pady=5)
        
        tk.Button(
            self.root, 
            text="Cerrar sesión", 
            width=30, 
            command=self.cerrar_sesion
        ).pack(pady=5)
        self.tree = ttk.Treeview(self.root, columns=("ID_usuario", "Username"), height=10)
        self.tree.heading("ID_usuario", text="ID_usuario")
        self.tree.heading("Username", text="Nombre de usuario")
        self.tree.pack(pady=10, padx=10, fill="both", expand=True)

        
    def ver_usuarios(self):
            # 1. CORRECCIÓN 1: Llamar al controlador, no a sí misma.
            usuarios = ver_usuarios()
            
            # Limpiar el Treeview
            for row in self.tree.get_children():
                self.tree.delete(row)
            
            # 'usuarios' es una lista como: [(1, 'admin'), (2, 'pepe')]
            
            for i in usuarios:
                # 'i' es la tupla, por ej: (1, 'admin')
                id_de_la_db = i[0] # Obtenemos el ID real (ej: 1)
                
                # 2. CORRECCIÓN 2: Usar 'iid=id_de_la_db'.
                #    Esto fuerza al Treeview a usar tu ID (1, 2, 3...)
                #    en lugar de 'I001', 'I002'...
                #    (También se corrigió el paréntesis faltante al final)
                self.tree.insert("", tk.END, iid=id_de_la_db, values=i)
    def agregar_usuarios(self):  
        def guardar():
            u = entry_user.get().strip()
            p = entry_pass.get().strip()
            if not u or not p:
                messagebox.showwarning("Campos vacíos", "Ingrese usuario y contraseña.")
                return
            if crear_usuarios(u, p):
                messagebox.showinfo("Éxito", f"Usuario {u} creado correctamente.")
                self.ver_usuarios()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo crear el usuario.")
        
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Usuario")
        ventana.geometry("300x200")
        tk.Label(ventana, text="Usuario").pack(pady=5)
        entry_user = tk.Entry(ventana)
        entry_user.pack(pady=5)
        tk.Label(ventana, text="Contraseña").pack(pady=5)
        entry_pass = tk.Entry(ventana, show="*")
        entry_pass.pack(pady=5)
        tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)
    # En cualquier parte dentro de tu clase UserView
# ...

    def actualizar_usuarios(self):
        # --- Prueba de depuración ---
        print("¡Botón de actualizar funciona!") 
    
           # 1. Obtener selección (necesita 'self.tree')
        selected_item = self.tree.focus() 
        if not selected_item:
            messagebox.showwarning("Sin selección", "Por favor, seleccione un usuario para editar.")
            return
        print(f"[VISTA] ID seleccionado: {selected_item} (Tipo: {type(selected_item)})")

        id_usuario = selected_item
        
            # 2. Obtener datos del controlador
        datos_usuario = obtener_usuario_por_id(id_usuario)
        if not datos_usuario:
            messagebox.showerror("Error", "No se pudieron obtener los datos del usuario.")
            return
        
        user_actual, pass_actual = datos_usuario

            # 3. Función interna (tu estilo)
        def guardar_cambios():
                u_nuevo = entry_user.get().strip()
                p_nuevo = entry_pass.get().strip()
            
                if not u_nuevo or not p_nuevo:
                    messagebox.showwarning("Campos vacíos", "Los campos no pueden estar vacíos.", parent=ventana_edit)
                    return
            
                if actualizar_usuario_por_id(id_usuario, u_nuevo, p_nuevo):
                    messagebox.showinfo("Éxito", f"Usuario {u_nuevo} actualizado.", parent=ventana_edit)
                    self.ver_usuarios() # Refrescar la lista
                    ventana_edit.destroy()
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el usuario.", parent=ventana_edit)
        
            # 4. Crear la ventana Toplevel
        ventana_edit = tk.Toplevel(self.root)
        ventana_edit.title(f"Editar Usuario (ID: {id_usuario})")
            # ... (resto del código de la ventana de edición) ...
        tk.Label(ventana_edit, text="Usuario").pack()
        entry_user = tk.Entry(ventana_edit)
        entry_user.pack()
        entry_user.insert(0, user_actual)
        
        tk.Label(ventana_edit, text="Contraseña").pack()
        entry_pass = tk.Entry(ventana_edit, show="*")
        entry_pass.pack()
        entry_pass.insert(0, pass_actual)
        
        tk.Button(ventana_edit, text="Actualizar", command=guardar_cambios).pack()

    def eliminar_usuarios(self):
        """
        Este es el método que se llama desde el botón "Eliminar".
        """
        # 1. Obtener el usuario seleccionado del Treeview
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Sin selección", "Por favor, seleccione un usuario para eliminar.")
            return

        # 2. Convertir el ID (que es string) a entero
        try:
            id_usuario = int(selected_item)
        except ValueError:
            messagebox.showerror("Error", "El ID seleccionado no es un número válido.")
            return
            
        # 3. (Opcional pero recomendado) Obtener el username para el mensaje
        try:
            username = self.tree.item(selected_item)['values'][1]
        except IndexError:
            username = "el usuario seleccionado" # Por si acaso

        # 4. PEDIR CONFIRMACIÓN (¡Muy importante!)
        if messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de que desea eliminar a '{username}' (ID: {id_usuario})?"):
            
            # 5. Llamar al controlador para eliminar
            if eliminar_usuario_por_id(id_usuario):
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
                # 6. Refrescar la lista para que se vea el cambio
                self.ver_usuarios()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el usuario.")
    
    def cerrar_sesion(self):
        
        respuesta = messagebox.askyesno("Cerrar Sesión", "¿Seguro que desea cerrar sesión?")
        
        if respuesta:
            self.root.destroy()
        else:
            messagebox.showinfo("Cancelado", "Sesión no cerrada.")

if __name__ == "__main__":
    App = DashboardApp("Irvin")
