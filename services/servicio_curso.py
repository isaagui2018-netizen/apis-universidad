"""
Servicio simple para cursos con polimorfismo
Usa mocks para retornar datos de ejemplo
"""
from typing import Dict, List, Any, Optional
from services.servicio_base import ServicioBase
from models.curso import Curso
from models.horario import Horario
from views.vista_curso import VistaCurso
from mocks.mocks_curso import MocksCurso
from datetime import time

class ServicioCurso(ServicioBase):
    """Servicio para gestionar cursos - Polimorfismo con Mocks"""
    
    def __init__(self):
        self._cursos: Dict[int, Curso] = {}
        self._contador_id = 1
        self.vista = VistaCurso()
        self.mocks = MocksCurso()
    
    def crear(self, datos: Dict[str, Any]) -> Dict[str, Any]:
        """POST - Crea un nuevo curso y retorna mock"""
        if 'nombre' not in datos:
            return self.vista.formatear_error("Falta el campo nombre", 400)
        
        # Crear curso real
        curso = Curso(
            nombre=datos['nombre'],
            codigo=datos.get('codigo', ''),
            creditos=datos.get('creditos', 0)
        )
        
        if 'horario' in datos:
            horario_data = datos['horario']
            horario = Horario(
                dia_semana=horario_data.get('dia_semana', ''),
                hora_inicio=time.fromisoformat(horario_data.get('hora_inicio', '08:00')),
                hora_fin=time.fromisoformat(horario_data.get('hora_fin', '10:00')),
                salon=horario_data.get('salon', '')
            )
            curso.asignar_horario(horario)
        
        self._cursos[self._contador_id] = curso
        self._contador_id += 1
        
        # Retornar mock de respuesta
        mock_respuesta = self.mocks.get_mock_curso_creado(datos)
        return self.vista.formatear_respuesta(mock_respuesta)
    
    def obtener_todos(self) -> List[Dict[str, Any]]:
        """GET - Obtiene todos los cursos y retorna mocks"""
        # Retornar mocks en lugar de datos reales
        mocks = self.mocks.get_mock_lista_cursos()
        return mocks
    
    def obtener_por_id(self, id: int) -> Optional[Dict[str, Any]]:
        """GET /api/cursos/<id> - Obtiene un curso por ID y retorna mock"""
        # Retornar mock según el ID
        mock = self.mocks.get_mock_curso_por_id(id)
        return mock
    
    def actualizar(self, id: int, datos: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """PUT - Actualiza un curso y retorna mock"""
        # Actualizar curso real si existe
        curso = self._cursos.get(id)
        if curso:
            if 'nombre' in datos:
                curso.nombre = datos['nombre']
            if 'codigo' in datos:
                curso.codigo = datos['codigo']
            if 'creditos' in datos:
                curso.creditos = datos['creditos']
        
        # Retornar mock de respuesta
        mock_respuesta = self.mocks.get_mock_curso_actualizado(id, datos)
        return mock_respuesta
    
    def eliminar(self, id: int) -> bool:
        """DELETE - Elimina un curso"""
        if id in self._cursos:
            del self._cursos[id]
            return True
        return False
