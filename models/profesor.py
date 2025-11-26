from typing import List, Optional, TYPE_CHECKING
from models.usuario import Usuario

if TYPE_CHECKING:
    from models.curso import Curso
    from models.facultad import Facultad

class Profesor(Usuario):
    def __init__(self, id: int, nombre: str, edad: int, sexo: str, documento: int,
                 correo: str, contraseña: str, especialidad: str):
        super().__init__(id, nombre, edad, sexo, documento, correo, contraseña, "Profesor")
        self.especialidad = especialidad
        self.cursos: List['Curso'] = []
        self.facultad_decano: Optional['Facultad'] = None
    
    def dictar_curso(self, curso: 'Curso'):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.asignar_profesor(self)
    
    def listar_cursos(self) -> List['Curso']:
        return self.cursos

