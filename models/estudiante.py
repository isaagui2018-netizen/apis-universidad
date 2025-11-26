from typing import List, TYPE_CHECKING
from models.usuario import Usuario

if TYPE_CHECKING:
    from models.curso import Curso
    from models.programa import Programa
    from models.nota_curso import NotaCurso
    from models.matricula_programa import MatriculaPrograma

class Estudiante(Usuario):
    def __init__(self, id: int, nombre: str, edad: int, sexo: str, documento: int,
                 correo: str, contraseña: str):
        super().__init__(id, nombre, edad, sexo, documento, correo, contraseña, "Estudiante")
        self.programas: List['Programa'] = []
        self.cursos: List['Curso'] = []
        self.notas_curso: List['NotaCurso'] = []
        self.matriculas_programa: List['MatriculaPrograma'] = []
    
    def inscribirse_curso(self, curso: 'Curso'):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.agregar_estudiante(self)
    
    def calcular_promedio_general(self) -> float:
        if not self.notas_curso:
            return 0.0
        suma_notas = sum(nota.get_valor() for nota in self.notas_curso)
        return suma_notas / len(self.notas_curso)

