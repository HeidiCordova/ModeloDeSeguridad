# Interfaces/pantalla_principal.py

import tkinter as tk
from tkinter import ttk

class PantallaPrincipal(tk.Frame):
    def __init__(self, parent, show_register_screen, show_login_screen):
        super().__init__(parent)
        self.parent = parent
        self.show_register_screen = show_register_screen
        self.show_login_screen = show_login_screen
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Bienvenido al Sistema de Control de Acceso", font=("Helvetica", 18)).pack(pady=20)
        ttk.Button(self, text="Registrarse", command=self.show_register_screen).pack(pady=10)
        ttk.Button(self, text="Iniciar Sesión", command=self.show_login_screen).pack(pady=10)
