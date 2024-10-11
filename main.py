# main.py
from permiso import Permiso
from rol import Rol

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

# Mostrar permisos de los roles
def mostrar_permisos_rol(rol):
    print(f"Rol: {rol.nombre}")
    for permiso in rol.permisos:
        print(f" - Permiso: {permiso.nombre}")

print("Permisos de los roles:")
mostrar_permisos_rol(rol_admin)
mostrar_permisos_rol(rol_usuario)
