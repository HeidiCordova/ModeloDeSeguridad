# Interfaces/pantalla_registro.py

import tkinter as tk
from tkinter import messagebox, ttk
from main import auth, rol_admin, rol_usuario

class PantallaRegistro(tk.Frame):
    def __init__(self, parent, show_main_screen):
        super().__init__(parent)
        self.parent = parent
        self.show_main_screen = show_main_screen
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Registro de Usuario", font=("Helvetica", 18)).pack(pady=20)
        
        ttk.Label(self, text="Nombre de Usuario:").pack()
        self.entry_nombre = ttk.Entry(self)
        self.entry_nombre.pack(pady=5)
        
        ttk.Label(self, text="Contraseña:").pack()
        self.entry_contrasena = ttk.Entry(self, show="*")
        self.entry_contrasena.pack(pady=5)
        
        ttk.Label(self, text="Seleccione Rol:").pack()
        self.rol_var = tk.StringVar(value="Usuario")
        ttk.Radiobutton(self, text="Administrador", variable=self.rol_var, value="Administrador").pack(pady=5)
        ttk.Radiobutton(self, text="Usuario", variable=self.rol_var, value="Usuario").pack(pady=5)
        
        ttk.Button(self, text="Registrar", command=self.registrar_usuario).pack(pady=10)
        ttk.Button(self, text="Volver", command=self.show_main_screen).pack(pady=10)

    def registrar_usuario(self):
        nombre = self.entry_nombre.get()
        contrasena = self.entry_contrasena.get()
        rol = rol_admin if self.rol_var.get() == "Administrador" else rol_usuario
        auth.registrar_usuario(nombre, contrasena, rol)
        messagebox.showinfo("Registro", f"Usuario '{nombre}' registrado exitosamente.")
        self.show_main_screen()
