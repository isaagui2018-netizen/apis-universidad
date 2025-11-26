
from flask import Flask, jsonify
from controllers.controlador_curso import ControladorCurso

app = Flask(__name__)

controlador = ControladorCurso()


@app.route('/api/cursos', methods=['GET'])
def listar_cursos():
    return controlador.listar()

@app.route('/api/cursos', methods=['POST'])
def crear_curso():
    return controlador.crear()

@app.route('/api/cursos/<int:id>', methods=['GET'])
def obtener_curso(id):
    return controlador.obtener(id)

@app.route('/api/cursos/<int:id>', methods=['PUT'])
def actualizar_curso(id):
    return controlador.actualizar(id)

@app.route('/api/cursos/<int:id>', methods=['DELETE'])
def eliminar_curso(id):
    return controlador.eliminar(id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
