# main.py
# main.py

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
#LOS ADMINISTRADORES TIENEN TODOS LOS PERMISOS: LEER, ESCRIBIR Y ELIMINAR
rol_admin.agregar_permiso(permiso_leer)
rol_admin.agregar_permiso(permiso_escribir)
rol_admin.agregar_permiso(permiso_eliminar)

#LOS USUARIOS SOLO TIENEN LOS PERMISOS DE LECTURA
rol_usuario.agregar_permiso(permiso_leer)

# Inicializar el sistema de autenticación
auth = Autenticacion()

# Registrar usuarios y asignarles roles
auth.registrar_usuario("Heidi", "password123", rol_admin)
auth.registrar_usuario("Jordy", "password456", rol_usuario)

# Función para verificar y mostrar permisos de un usuario autenticado
def verificar_permiso_usuario(usuario, permiso):
    if usuario.tiene_permiso_en_rol(permiso):
        print(f"{usuario.nombre} tiene permiso para {permiso.nombre}.")
    else:
        print(f"{usuario.nombre} NO tiene permiso para {permiso.nombre}.")




##PROBANDO AUTENTICACIÓN
# Autenticar y verificar permisos de usuarios
print("\n\n***Intentando autenticar a los usuarios****\n")



# Autenticación de Heidi (administrador)
usuario_autenticado = auth.autenticar("Heidi", "password123")
if usuario_autenticado:
    print(f"Usuario '{usuario_autenticado.nombre}' autenticado exitosamente.")
    verificar_permiso_usuario(usuario_autenticado, permiso_leer)
    verificar_permiso_usuario(usuario_autenticado, permiso_escribir)
    verificar_permiso_usuario(usuario_autenticado, permiso_eliminar)
else:
    print("No se pudo autenticar a Heidi.")




# Autenticación de Jordy (usuario)
usuario_autenticado = auth.autenticar("Jordy", "password456")
if usuario_autenticado:
    print(f"\nUsuario '{usuario_autenticado.nombre}' autenticado exitosamente.")
    verificar_permiso_usuario(usuario_autenticado, permiso_leer)
    verificar_permiso_usuario(usuario_autenticado, permiso_escribir)  # Jordy no debería tener permiso para escribir
else:
    print("No se pudo autenticar a Jordy.")
