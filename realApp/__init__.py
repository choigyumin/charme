from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/keyboard', methods=['GET'])
def keyboard():
  # user input keyboard !
  # type of text (default)
  # and button... 
  server_to_user_data = {
    'type': 'buttons',
    'buttons': [
      "견적문의", 
      "후기남기기", 
      "별점주기"
      ]
    }
  return jsonify(server_to_user_data)

@app.route('/message', methods=['POST'])
def message():

  data_from_user = request.get_json()
  content = data_from_user['content']

  # 견적문의
  if content == u"견적문의":
    data_to_user = {
      "message": {
        "text": "예식 날짜, 시간과 장소를 남겨주시면 빠른 시간 내에 견적을 알려드리도록 하겠습니다. 감사합니다. 끝이라고 입력하시면 처음 메뉴로 돌아갑니다."
      },
      "keyboard": {
        'type': 'text'
      }
    }
  elif content == u"후기남기기":
    data_to_user = {
      "message": {
        "message_button": {
          "label": "후기를 남겨주시면 저희에게 큰 힘이 됩니다! 후기남기러 가기",
          "url": "http://charme.co.kr"
        }
      }
    }
    # 작동 테스트 완료
  elif u"끝" in content:
    data_to_user = {
      "keyboard": {
        'type': 'buttons',
        'buttons': [
        "견적문의", 
        "후기남기기", 
        "별점주기"
        ]
      }
    }
  elif u"*" in content:
    data_to_user = {
      "keyboard": {
        'type': 'buttons',
        'buttons': [
        "견적문의", 
        "후기남기기", 
        "별점주기"
        ]
      }
    }
  elif content== u"별점주기": # 별점주기
    data_to_user = {
      "keyboard": {
        "type": "buttons",
        "buttons": [
          "* 매우만족",
          "* 만족", 
          "* 보통", 
          "* 실망"
        ]
      }
    }


  return jsonify(data_to_user)

# 견적문의: 견적 양식 텍스트 return,
# 후기남기기: 후기 양식 텍스트 return..
# 여기에 별점 버튼도 포함 !

