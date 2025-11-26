
from typing import Dict, List, Any
from models.curso import Curso
from models.horario import Horario
from datetime import time

class MocksCurso:
    
    @staticmethod
    def get_mock_lista_cursos() -> List[Dict[str, Any]]:
        return [
            {
                "nombre": "Programación I",
                "codigo": "PROG101",
                "creditos": 4,
                "cantidad_estudiantes": 25,
                "promedio_curso": 3.8,
                "profesor": "Dr. Juan Pérez",
                "horario": {
                    "dia_semana": "Lunes",
                    "hora_inicio": "08:00:00",
                    "hora_fin": "10:00:00",
                    "salon": "A-101"
                }
            },
            {
                "nombre": "Base de Datos",
                "codigo": "BD201",
                "creditos": 3,
                "cantidad_estudiantes": 30,
                "promedio_curso": 4.2,
                "profesor": "Dra. María García",
                "horario": {
                    "dia_semana": "Miércoles",
                    "hora_inicio": "14:00:00",
                    "hora_fin": "16:00:00",
                    "salon": "B-205"
                }
            },
            {
                "nombre": "Estructuras de Datos",
                "codigo": "ED301",
                "creditos": 4,
                "cantidad_estudiantes": 20,
                "promedio_curso": 3.5,
                "profesor": "Dr. Carlos López",
                "horario": {
                    "dia_semana": "Viernes",
                    "hora_inicio": "10:00:00",
                    "hora_fin": "12:00:00",
                    "salon": "C-301"
                }
            }
        ]
    
    @staticmethod
    def get_mock_curso_por_id(id: int) -> Dict[str, Any]:
        mocks = {
            1: {
                "nombre": "Programación I",
                "codigo": "PROG101",
                "creditos": 4,
                "cantidad_estudiantes": 25,
                "promedio_curso": 3.8,
                "profesor": "Dr. Juan Pérez",
                "horario": {
                    "dia_semana": "Lunes",
                    "hora_inicio": "08:00:00",
                    "hora_fin": "10:00:00",
                    "salon": "A-101"
                }
            },
            2: {
                "nombre": "Base de Datos",
                "codigo": "BD201",
                "creditos": 3,
                "cantidad_estudiantes": 30,
                "promedio_curso": 4.2,
                "profesor": "Dra. María García",
                "horario": {
                    "dia_semana": "Miércoles",
                    "hora_inicio": "14:00:00",
                    "hora_fin": "16:00:00",
                    "salon": "B-205"
                }
            },
            3: {
                "nombre": "Estructuras de Datos",
                "codigo": "ED301",
                "creditos": 4,
                "cantidad_estudiantes": 20,
                "promedio_curso": 3.5,
                "profesor": "Dr. Carlos López",
                "horario": {
                    "dia_semana": "Viernes",
                    "hora_inicio": "10:00:00",
                    "hora_fin": "12:00:00",
                    "salon": "C-301"
                }
            }
        }
        return mocks.get(id, None)
    
    @staticmethod
    def get_mock_curso_creado(datos: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "nombre": datos.get('nombre', 'Nuevo Curso'),
            "codigo": datos.get('codigo', 'COD001'),
            "creditos": datos.get('creditos', 3),
            "cantidad_estudiantes": 0,
            "promedio_curso": 0.0,
            "profesor": datos.get('profesor', None),
            "horario": datos.get('horario', None)
        }
    
    @staticmethod
    def get_mock_curso_actualizado(id: int, datos: Dict[str, Any]) -> Dict[str, Any]:
        curso_base = MocksCurso.get_mock_curso_por_id(id)
        if not curso_base:
            return None
        
        curso_base.update({
            "nombre": datos.get('nombre', curso_base['nombre']),
            "codigo": datos.get('codigo', curso_base['codigo']),
            "creditos": datos.get('creditos', curso_base['creditos'])
        })
        return curso_base
    
    @staticmethod
    def crear_objetos_curso_mock() -> List[Curso]:
        cursos = []
        
        # Curso 1
        curso1 = Curso("Programación I", "PROG101", 4)
        horario1 = Horario("Lunes", time(8, 0), time(10, 0), "A-101")
        curso1.asignar_horario(horario1)
        cursos.append(curso1)
        
        # Curso 2
        curso2 = Curso("Base de Datos", "BD201", 3)
        horario2 = Horario("Miércoles", time(14, 0), time(16, 0), "B-205")
        curso2.asignar_horario(horario2)
        cursos.append(curso2)
        
        # Curso 3
        curso3 = Curso("Estructuras de Datos", "ED301", 4)
        horario3 = Horario("Viernes", time(10, 0), time(12, 0), "C-301")
        curso3.asignar_horario(horario3)
        cursos.append(curso3)
        
        return cursos

