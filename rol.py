# rol.py
from permiso import Permiso

class Rol:
    def __init__(self, nombre):
        self.nombre = nombre
        self.permisos = []

    def agregar_permiso(self, permiso):
        if permiso not in self.permisos:
            self.permisos.append(permiso)

    def eliminar_permiso(self, permiso):
        if permiso in self.permisos:
            self.permisos.remove(permiso)

    def tiene_permiso(self, permiso):
        return permiso in self.permisos
