from typing import Optional
from datetime import time

class Horario:
    def __init__(self, dia_semana: str, hora_inicio: time, hora_fin: time, salon: str):
        self.dia_semana = dia_semana
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.salon = salon
        self.curso: Optional['Curso'] = None
    
    def mostrar_horario(self):
        print(f"Día: {self.dia_semana}")
        print(f"Hora inicio: {self.hora_inicio}")
        print(f"Hora fin: {self.hora_fin}")
        print(f"Salón: {self.salon}")

