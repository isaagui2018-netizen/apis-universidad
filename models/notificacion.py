from typing import List
from datetime import date

class Notificacion:
    def __init__(self, id_notificacion: int, mensaje: str, fecha_envio: date):
        self.id_notificacion = id_notificacion
        self.mensaje = mensaje
        self.fecha_envio = fecha_envio
        self.leida = False
        self.usuarios: List['Usuario'] = []
    
    def enviar(self):
        for usuario in self.usuarios:
            usuario.agregar_notificacion(self)
            print(f"Notificación enviada a {usuario.nombre}")
    
    def marcar_como_leida(self):
        self.leida = True
    
    def mostrar(self):
        estado = "Leída" if self.leida else "No leída"
        print(f"ID: {self.id_notificacion}")
        print(f"Mensaje: {self.mensaje}")
        print(f"Fecha: {self.fecha_envio}")
        print(f"Estado: {estado}")
    
    def agregar_usuario(self, usuario: 'Usuario'):
        if usuario not in self.usuarios:
            self.usuarios.append(usuario)

