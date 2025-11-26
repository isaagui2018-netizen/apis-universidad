"""
Servicio base con polimorfismo
Define la interfaz común que todos los servicios deben implementar
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class ServicioBase(ABC):
    """Clase abstracta base para todos los servicios - Polimorfismo"""
    
    @abstractmethod
    def crear(self, datos: Dict[str, Any]) -> Dict[str, Any]:
        """Crea un nuevo recurso"""
        pass
    
    @abstractmethod
    def obtener_todos(self) -> List[Dict[str, Any]]:
        """Obtiene todos los recursos"""
        pass
    
    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[Dict[str, Any]]:
        """Obtiene un recurso por su ID"""
        pass
    
    @abstractmethod
    def actualizar(self, id: int, datos: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Actualiza un recurso existente"""
        pass
    
    @abstractmethod
    def eliminar(self, id: int) -> bool:
        """Elimina un recurso"""
        pass
    
    def validar_datos(self, datos: Dict[str, Any], campos_requeridos: List[str]) -> bool:
        """Método común para validar datos - puede ser sobrescrito"""
        return all(campo in datos for campo in campos_requeridos)

