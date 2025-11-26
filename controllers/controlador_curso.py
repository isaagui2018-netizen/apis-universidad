
from flask import request, jsonify
from services.servicio_curso import ServicioCurso
from views.vista_curso import VistaCurso

class ControladorCurso:

    
    def __init__(self):
        self.servicio = ServicioCurso()
        self.vista = VistaCurso()
    
    def listar(self):
        cursos = self.servicio.obtener_todos()
        return jsonify(self.vista.formatear_respuesta(cursos))
    
    def crear(self):
        datos = request.get_json() or {}
        resultado = self.servicio.crear(datos)
        if resultado.get('success'):
            return jsonify(resultado), 201
        return jsonify(resultado), resultado.get('codigo', 400)
    
    def obtener(self, id: int):
        curso = self.servicio.obtener_por_id(id)
        if curso:
            return jsonify(self.vista.formatear_respuesta(curso))
        return jsonify(self.vista.formatear_error("Curso no encontrado", 404)), 404
    
    def actualizar(self, id: int):
        datos = request.get_json() or {}
        curso = self.servicio.actualizar(id, datos)
        if curso:
            return jsonify(self.vista.formatear_respuesta(curso))
        return jsonify(self.vista.formatear_error("Curso no encontrado", 404)), 404
    
    def eliminar(self, id: int):
        if self.servicio.eliminar(id):
            return '', 204
        return jsonify(self.vista.formatear_error("Curso no encontrado", 404)), 404
