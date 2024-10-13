# Interfaces/pantalla_login.py

import tkinter as tk
from tkinter import messagebox, ttk
from main import auth

class PantallaLogin(tk.Frame):
    def __init__(self, parent, show_permissions_screen, show_main_screen):
        super().__init__(parent)
        self.parent = parent
        self.show_permissions_screen = show_permissions_screen
        self.show_main_screen = show_main_screen
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Inicio de Sesión", font=("Helvetica", 18)).pack(pady=20)
        
        ttk.Label(self, text="Nombre de Usuario:").pack()
        self.entry_nombre = ttk.Entry(self)
        self.entry_nombre.pack(pady=5)
        
        ttk.Label(self, text="Contraseña:").pack()
        self.entry_contrasena = ttk.Entry(self, show="*")
        self.entry_contrasena.pack(pady=5)
        
        ttk.Button(self, text="Iniciar Sesión", command=self.autenticar_usuario).pack(pady=10)
        ttk.Button(self, text="Volver", command=self.show_main_screen).pack(pady=10)

    def autenticar_usuario(self):
        nombre = self.entry_nombre.get()
        contrasena = self.entry_contrasena.get()
        usuario = auth.autenticar(nombre, contrasena)
        if usuario:
            self.show_permissions_screen(usuario)
        else:
            messagebox.showerror("Error", "Autenticación fallida. Verifique sus credenciales.")
            #
