from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/keyboard', methods=['GET'])
def keyboard():
  return jsonify({'type': 'button',\
                  'buttons': ["견적문의", "후기남기기", "별점주기"]
                  })

@app.route('/message', methods=['POST'])
def message():

  content = request.json['content']
  response = content

  return jsonify({\
                  'type': 'button',\
                  'buttons': ["견적문의", "후기남기기", "별점주기"]
                  })

# TODO: have to change for counselings...
# 견적문의: 견적 양식 텍스트 return,
# 후기남기기: 후기 양식 텍스트 return..
# 여기에 별점 버튼도 포함 !
# 별점주기: 별점 버튼 5개 return.

