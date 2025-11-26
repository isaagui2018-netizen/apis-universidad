from typing import List, Optional, TYPE_CHECKING
from models.ubicacion import Ubicacion
from models.universidad import Universidad

if TYPE_CHECKING:
    from models.programa import Programa

class Facultad:
    def __init__(self, nombre: str, codigo: str):
        self.nombre = nombre
        self.codigo = codigo
        self.decano: Optional['Profesor'] = None
        self.ubicacion: Optional[Ubicacion] = None
        self.universidad: Optional[Universidad] = None
        self.programas: List['Programa'] = []
    
    def agregar_programa(self, programa: 'Programa'):
        if programa not in self.programas:
            self.programas.append(programa)
            programa.facultad = self
    
    def obtener_programas(self) -> List['Programa']:
        return self.programas
    
    def asignar_decano(self, profesor):
        from models.profesor import Profesor
        self.decano = profesor
        profesor.facultad_decano = self
    
    def asignar_ubicacion(self, ubicacion: Ubicacion):
        self.ubicacion = ubicacion
        ubicacion.facultad = self

