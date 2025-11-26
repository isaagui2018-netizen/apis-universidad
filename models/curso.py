from typing import List, Optional
from models.horario import Horario
from models.profesor import Profesor
from models.estudiante import Estudiante
from models.programa import Programa
from models.nota_curso import NotaCurso

class Curso:
    def __init__(self, nombre: str, codigo: str, creditos: int):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.profesor: Optional['Profesor'] = None
        self.estudiantes: List['Estudiante'] = []
        self.horario: Optional[Horario] = None
        self.programa: Optional['Programa'] = None
        self.notas_curso: List['NotaCurso'] = []
    
    def asignar_profesor(self, profesor: 'Profesor'):
        self.profesor = profesor
        if self not in profesor.cursos:
            profesor.cursos.append(self)
    
    def agregar_estudiante(self, estudiante: 'Estudiante'):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)
            if self not in estudiante.cursos:
                estudiante.cursos.append(self)
    
    def registrar_nota(self, nota: 'NotaCurso'):
        if nota not in self.notas_curso:
            self.notas_curso.append(nota)
            nota.curso = self
            if nota not in nota.estudiante.notas_curso:
                nota.estudiante.notas_curso.append(nota)
    
    def calcular_promedio(self) -> float:
        if not self.notas_curso:
            return 0.0
        suma_notas = sum(nota.get_valor() for nota in self.notas_curso)
        return suma_notas / len(self.notas_curso)
    
    def asignar_horario(self, horario: Horario):
        self.horario = horario
        horario.curso = self

