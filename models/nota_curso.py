from typing import Optional, TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from models.curso import Curso
    from models.estudiante import Estudiante

class NotaCurso:
    def __init__(self, valor: float, fecha: date, tipo: str):
        self.valor = valor
        self.fecha = fecha
        self.tipo = tipo
        self.curso: Optional['Curso'] = None
        self.estudiante: Optional['Estudiante'] = None
    
    def get_valor(self) -> float:
        return self.valor
    
    def set_valor(self, v: float):
        self.valor = v

