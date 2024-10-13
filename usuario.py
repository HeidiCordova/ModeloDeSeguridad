from rol import Rol

#Creación de la clase Usuario, esta sirve para definir los usuarios y verificar si se tiene un permiso

class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def tiene_permiso_en_rol(self, permiso):
        return self.rol.tiene_permiso(permiso)

# Ejemplo de uso:
# usuario_admin = Usuario("Alice", rol_admin)
# if usuario_admin.tiene_permiso(permiso_leer):
#     print("El usuario tiene permiso para leer.")
