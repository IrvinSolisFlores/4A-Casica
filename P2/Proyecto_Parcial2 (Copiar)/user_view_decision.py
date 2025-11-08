import tkinter as tk
from tkinter import messagebox
from user_view import DashboardApp
from productos_view import DashboardProductos

class prod:
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario  # 👈 guardamos el usuario recibido
        self.root.title("Qué deseas hacer")
        self.root.geometry("400x300")
        self.root.resizable(True, True)
        
        # Encabezado
        tk.Label(root, text=f"Selecciona un campo, {self.usuario}", font=("Arial", 16, "bold")).pack(pady=20)
        
        # Botones
        tk.Button(root, text="Usuarios", command=self.usuarios).pack(pady=20)
        tk.Button(root, text="Productos", command=self.productos).pack(pady=20)

    def productos(self):
        messagebox.showinfo("Opción", "Excelente, presiona OK para pasar al menú de productos.")
        self.root.destroy()
        DashboardProductos(self.usuario)

    def usuarios(self):
        messagebox.showinfo("Opción", "Accediendo al menú de usuarios.")
        self.root.destroy()

        # 👇 Creamos la siguiente ventana pasando el usuario
        DashboardApp(self.usuario)

# --- Esto inicializa la ventana principal SOLO si lo ejecutas directamente ---
if __name__ == "__main__":
    root = tk.Tk()
    app = prod(root, "admin")  # 👈 para probar directamente
    root.mainloop()

