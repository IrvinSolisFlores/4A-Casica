import tkinter as tk
from tkinter import messagebox
from auth_controller import validar_credenciales
from user_view import DashboardApp
from user_view_decision import prod
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de sesión")
        self.root.geometry("400x300")
        self.root.resizable(True, True)
        
        # Encabezado
        tk.Label(root, text="Bienvenido al sistema", font=("Arial", 16, "bold")).pack(pady=20)
        
        # Campo de usuario
        tk.Label(root, text="Ingresa tu nombre de usuario:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)
       
        # Campo de contraseña
        tk.Label(root, text="Ingresa tu contraseña:").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)
       
        # Botón de inicio de sesión
        tk.Button(root, text="Iniciar sesión", command=self.login).pack(pady=20)
    def login(self):
        usuario = self.username_entry.get().strip()
        contrasena = self.password_entry.get().strip()
        
        if not usuario or not contrasena:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return
        
        if validar_credenciales(usuario, contrasena):
            messagebox.showinfo("Bienvenido", f"Hola {usuario}, acceso concedido.")
            self.root.destroy()
            new_root = tk.Tk()
            prod(new_root, usuario)
            new_root.mainloop()##funcion que muestra la segunda opcion
            
        else:
            messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos.")


