from typing import List

class Universidad:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion
        self.facultades: List['Facultad'] = []
    
    def agregar_facultad(self, facultad: 'Facultad'):
        if facultad not in self.facultades:
            self.facultades.append(facultad)
            facultad.universidad = self
    
    def obtener_facultades(self) -> List['Facultad']:
        return self.facultades

