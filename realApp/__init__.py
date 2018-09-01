from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/keyboard', methods=['GET'])
def keyboard():
  return jsonify({'type': 'text'})

@app.route('/message', methods=['POST'])
def message():
  content = request.json['content']
  response = content

  return jsonify(
      {
          'message': {
              'text': response
          },
          'keyboard': {
              'type': 'text'
          }

      })


