# autenticacion.py

from usuario import Usuario

class Autenticacion:
    def __init__(self):
        # Con este diccionario se almacenan los usuarios y sus datos
        self.usuarios_registrados = {}

    def registrar_usuario(self, nombre, contrasena, rol):
        # Crea un nuevo usuario con su rol y almacena la contraseña
        if nombre not in self.usuarios_registrados:
            usuario = Usuario(nombre, rol)
            self.usuarios_registrados[nombre] = {"usuario": usuario, "contrasena": contrasena}
            print(f"Usuario '{nombre}' registrado exitosamente.")
        else:
            print(f"El usuario '{nombre}' ya está registrado.")

    def autenticar(self, nombre, contrasena):
        # Verifica si el usuario existe y la contraseña es correcta
        if nombre in self.usuarios_registrados:
            if self.usuarios_registrados[nombre]["contrasena"] == contrasena:
                print(f"Usuario '{nombre}' autenticado correctamente.")
                return self.usuarios_registrados[nombre]["usuario"]
            else:
                print("Contraseña incorrecta.")
        else:
            print("El usuario no está registrado.")
        return None
