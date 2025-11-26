from typing import List, Optional, TYPE_CHECKING
from models.facultad import Facultad

if TYPE_CHECKING:
    from models.curso import Curso
    from models.matricula_programa import MatriculaPrograma
    from models.estudiante import Estudiante

class Programa:
    def __init__(self, nombre: str, codigo: str):
        self.nombre = nombre
        self.codigo = codigo
        self.cursos: List['Curso'] = []
        self.facultad: Optional[Facultad] = None
        self.matriculas: List['MatriculaPrograma'] = []
    
    def agregar_curso(self, curso: 'Curso'):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.programa = self
    
    def inscribir_estudiante(self, estudiante):
        from models.matricula_programa import MatriculaPrograma
        from datetime import date
        matricula = MatriculaPrograma(
            estudiante=estudiante,
            programa=self,
            fecha_inscripcion=date.today(),
            modalidad="Presencial"
        )
        self.matriculas.append(matricula)
        estudiante.matriculas_programa.append(matricula)
    
    def obtener_promedios(self) -> float:
        if not self.matriculas:
            return 0.0
        promedios = [matricula.promedio for matricula in self.matriculas if matricula.promedio is not None]
        if not promedios:
            return 0.0
        return sum(promedios) / len(promedios)

