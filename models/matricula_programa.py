from typing import Optional, TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from models.estudiante import Estudiante
    from models.programa import Programa

class MatriculaPrograma:
    def __init__(self, estudiante: 'Estudiante', programa: 'Programa', 
                 fecha_inscripcion: date, modalidad: str):
        self.promedio: Optional[float] = None
        self.fecha_inscripcion = fecha_inscripcion
        self.modalidad = modalidad
        self.estudiante = estudiante
        self.programa = programa
        
        if self not in estudiante.matriculas_programa:
            estudiante.matriculas_programa.append(self)
        if self not in programa.matriculas:
            programa.matriculas.append(self)
    
    def inscribir_estudiante(self, estudiante: 'Estudiante'):
        self.estudiante = estudiante
        if self not in estudiante.matriculas_programa:
            estudiante.matriculas_programa.append(self)
    
    def obtener_promedios(self) -> float:
        if self.promedio is not None:
            return self.promedio
        notas_programa = [
            nota for nota in self.estudiante.notas_curso 
            if nota.curso and nota.curso.programa == self.programa
        ]
        if not notas_programa:
            return 0.0
        suma_notas = sum(nota.get_valor() for nota in notas_programa)
        self.promedio = suma_notas / len(notas_programa)
        return self.promedio

