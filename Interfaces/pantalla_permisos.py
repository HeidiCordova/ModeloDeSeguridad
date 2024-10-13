# Interfaces/pantalla_permisos.py

import tkinter as tk
from tkinter import ttk
from main import permiso_leer, permiso_escribir, permiso_eliminar

class PantallaPermisos(tk.Frame):
    def __init__(self, parent, usuario, show_main_screen):
        super().__init__(parent)
        self.parent = parent
        self.usuario = usuario
        self.show_main_screen = show_main_screen
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text=f"Bienvenido, {self.usuario.nombre}", font=("Helvetica", 18)).pack(pady=20)
        ttk.Label(self, text="Permisos asignados:", font=("Helvetica", 14)).pack(pady=10)
        
        permisos = []
        if self.usuario.tiene_permiso_en_rol(permiso_leer):
            permisos.append("Leer")
        if self.usuario.tiene_permiso_en_rol(permiso_escribir):
            permisos.append("Escribir")
        if self.usuario.tiene_permiso_en_rol(permiso_eliminar):
            permisos.append("Eliminar")
        
        permisos_str = "\n".join(permisos) if permisos else "Sin permisos asignados."
        ttk.Label(self, text=permisos_str, font=("Helvetica", 12)).pack(pady=10)
        
        ttk.Button(self, text="Cerrar Sesión", command=self.show_main_screen).pack(pady=20)
 