from typing import List
from datetime import date

class Usuario:
    def __init__(self, id: int, nombre: str, edad: int, sexo: str, documento: int, 
                 correo: str, contraseña: str, tipo: str):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.documento = documento
        self.correo = correo
        self.contraseña = contraseña
        self.tipo = tipo
        self.notificaciones: List['Notificacion'] = []
    
    def mostrar_perfil(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Documento: {self.documento}")
        print(f"Correo: {self.correo}")
        print(f"Tipo: {self.tipo}")
    
    def iniciar_sesion(self, correo: str, contraseña: str) -> bool:
        return self.correo == correo and self.contraseña == contraseña
    
    def cerrar_sesion(self):
        print(f"Usuario {self.nombre} ha cerrado sesión")
    
    def actualizar_datos(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
    
    def agregar_notificacion(self, notificacion: 'Notificacion'):
        self.notificaciones.append(notificacion)

