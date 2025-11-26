
from typing import Dict, Any
from models.curso import Curso

class VistaCurso:
    
    @staticmethod
    def formatear_respuesta(datos: Any) -> Dict[str, Any]:
        return {"success": True, "data": datos}
    
    @staticmethod
    def formatear_error(mensaje: str, codigo: int = 400) -> Dict[str, Any]:
        return {"success": False, "error": mensaje, "codigo": codigo}
    
    @staticmethod
    def formatear_curso(curso: Curso) -> Dict:
        datos = {
            "nombre": curso.nombre,
            "codigo": curso.codigo,
            "creditos": curso.creditos,
            "cantidad_estudiantes": len(curso.estudiantes),
            "promedio_curso": curso.calcular_promedio()
        }
        
        if curso.profesor:
            datos["profesor"] = curso.profesor.nombre
        
        if curso.horario:
            datos["horario"] = {
                "dia_semana": curso.horario.dia_semana,
                "hora_inicio": str(curso.horario.hora_inicio),
                "hora_fin": str(curso.horario.hora_fin),
                "salon": curso.horario.salon
            }
        
        return datos
