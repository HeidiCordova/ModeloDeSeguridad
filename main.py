# main.py

import tkinter as tk
from tkinter import messagebox, ttk
from permiso import Permiso
from rol import Rol
from usuario import Usuario
from autenticacion import Autenticacion

# Definir permisos
permiso_leer = Permiso("leer")
permiso_escribir = Permiso("escribir")
permiso_eliminar = Permiso("eliminar")

# Definir roles
rol_admin = Rol("administrador")
rol_usuario = Rol("usuario")

# Asignar permisos a roles
rol_admin.agregar_permiso(permiso_leer)
rol_admin.agregar_permiso(permiso_escribir)
rol_admin.agregar_permiso(permiso_eliminar)
rol_usuario.agregar_permiso(permiso_leer)

# Inicializar el sistema de autenticación
auth = Autenticacion()

# Registrar algunos usuarios de ejemplo
auth.registrar_usuario("Heidi", "password123", rol_admin)
auth.registrar_usuario("Jordy", "password456", rol_usuario)

# Clase de la aplicación completa con todas las pantallas integradas
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Control de Acceso")
        self.geometry("500x400")
        
        # Configuración de estilo general
        self.configure(bg="#282a36")
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        
        # Colores personalizados para los widgets
        self.style.configure("TLabel", foreground="white", background="#282a36", font=("Helvetica", 12))
        self.style.configure("TButton", font=("Helvetica", 10), padding=6, relief="flat")
        self.style.map("TButton", background=[("active", "#6272a4"), ("!disabled", "#44475a")], foreground=[("!disabled", "white")])
        
        self.show_main_screen()

    def show_main_screen(self):
        self.clear_frame()
        ttk.Label(self, text="Bienvenido al Sistema de Control de Acceso", font=("Helvetica", 18, "bold")).pack(pady=20)
        ttk.Button(self, text="Registrarse", command=self.show_register_screen).pack(pady=10)
        ttk.Button(self, text="Iniciar Sesión", command=self.show_login_screen).pack(pady=10)

    def show_register_screen(self):
        self.clear_frame()
        ttk.Label(self, text="Registro de Usuario", font=("Helvetica", 18, "bold")).pack(pady=20)
        
        ttk.Label(self, text="Nombre de Usuario:").pack()
        entry_nombre = ttk.Entry(self)
        entry_nombre.pack(pady=5)
        
        ttk.Label(self, text="Contraseña:").pack()
        entry_contrasena = ttk.Entry(self, show="*")
        entry_contrasena.pack(pady=5)
        
        ttk.Label(self, text="Seleccione Rol:").pack()
        rol_var = tk.StringVar(value="Usuario")
        ttk.Radiobutton(self, text="Administrador", variable=rol_var, value="Administrador").pack(pady=5)
        ttk.Radiobutton(self, text="Usuario", variable=rol_var, value="Usuario").pack(pady=5)
        
        def registrar_usuario():
            nombre = entry_nombre.get()
            contrasena = entry_contrasena.get()
            rol = rol_admin if rol_var.get() == "Administrador" else rol_usuario
            auth.registrar_usuario(nombre, contrasena, rol)
            messagebox.showinfo("Registro", f"Usuario '{nombre}' registrado exitosamente.")
            self.show_main_screen()

        ttk.Button(self, text="Registrar", command=registrar_usuario).pack(pady=10)
        ttk.Button(self, text="Volver", command=self.show_main_screen).pack(pady=10)

    def show_login_screen(self):
        self.clear_frame()
        ttk.Label(self, text="Inicio de Sesión", font=("Helvetica", 18, "bold")).pack(pady=20)
        
        ttk.Label(self, text="Nombre de Usuario:").pack()
        entry_nombre = ttk.Entry(self)
        entry_nombre.pack(pady=5)
        
        ttk.Label(self, text="Contraseña:").pack()
        entry_contrasena = ttk.Entry(self, show="*")
        entry_contrasena.pack(pady=5)
        
        def autenticar_usuario():
            nombre = entry_nombre.get()
            contrasena = entry_contrasena.get()
            usuario = auth.autenticar(nombre, contrasena)
            if usuario:
                self.show_permissions_screen(usuario)
            else:
                messagebox.showerror("Error", "Autenticación fallida. Verifique sus credenciales.")

        ttk.Button(self, text="Iniciar Sesión", command=autenticar_usuario).pack(pady=10)
        ttk.Button(self, text="Volver", command=self.show_main_screen).pack(pady=10)

    def show_permissions_screen(self, usuario):
        self.clear_frame()
        ttk.Label(self, text=f"Bienvenido, {usuario.nombre}", font=("Helvetica", 18, "bold")).pack(pady=20)
        ttk.Label(self, text="Permisos asignados:", font=("Helvetica", 14)).pack(pady=10)
        
        permisos = []
        if usuario.tiene_permiso_en_rol(permiso_leer):
            permisos.append("Leer")
        if usuario.tiene_permiso_en_rol(permiso_escribir):
            permisos.append("Escribir")
        if usuario.tiene_permiso_en_rol(permiso_eliminar):
            permisos.append("Eliminar")
        
        permisos_str = "\n".join(permisos) if permisos else "Sin permisos asignados."
        ttk.Label(self, text=permisos_str, font=("Helvetica", 12)).pack(pady=10)
        
        ttk.Button(self, text="Cerrar Sesión", command=self.show_main_screen).pack(pady=20)

    def clear_frame(self):
        # Elimina los widgets de la pantalla actual
        for widget in self.winfo_children():
            widget.destroy()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = App()
    app.mainloop()