from typing import Optional

class Ubicacion:
    def __init__(self, ciudad: str, direccion: str, barrio: str, latitud: int, longitud: int):
        self.ciudad = ciudad
        self.direccion = direccion
        self.barrio = barrio
        self.latitud = latitud
        self.longitud = longitud
        self.facultad: Optional['Facultad'] = None
    
    def obtener_direccion(self) -> str:
        return f"{self.direccion}, {self.barrio}, {self.ciudad}"

