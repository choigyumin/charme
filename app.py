from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/keyboard', methods=['GET'])
def keyboard():
    return jsonify({'type': 'text'})

if __name__ == '__main__':
    app.run(host='localhost', port=8082)
