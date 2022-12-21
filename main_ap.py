from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    # Obtiene los datos enviados en la petición
    data = request.get_json()

    # Procesa los datos (por ejemplo, guardándolos en una base de datos)
    name = data['name']
    email = data['email']
    # ...

    # Devuelve una respuesta al cliente
    response = {'status': 'success'}
    return jsonify(response)

if __name__ == '__main__':
    app.run()
