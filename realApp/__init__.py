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
      'keyboard': {
        'type': 'buttons',
        'buttons': [
        "견적문의", 
        "후기남기기", 
        "별점주기"
        ]
      },
      'message': {
        'text': "처음 메뉴로 돌아갑니다."
      }
    }
  elif u"****" in content: # 매우만족
    data_to_user = {
      'keyboard': {
        'type': 'buttons',
        'buttons': [
        "견적문의", 
        "후기남기기", 
        "별점주기"
        ]
      },
      'message': {
        'text': "좋은 평가 감사드립니다. 더 좋은 음악으로 보답하겠습니다."
      }
    }
  elif u"*" in content: # 보통,실망
    data_to_user = {
      'keyboard': {
        'type': 'buttons',
        'buttons': [
        "견적문의", 
        "후기남기기", 
        "별점주기"
        ]
      },
      'message': { 
        'text': "미흡한 점이 있었다면 진심으로 사과드립니다. 더 나은 샤르메가 되도록 노력하겠습니다. "
      }
    }
  elif content== u"별점주기": # 별점주기
    data_to_user = {
      "keyboard": {
        'type': 'buttons',
        'buttons': [
          "***** 매우만족",
          "****  만족", 
          "***   보통", 
          "*     실망"
        ]
      },
      'message': {
        'text': "소개시켜주고 싶은 샤르메가 되겠습니다."
      }
    }


  return jsonify(data_to_user)

# 견적문의: 견적 양식 텍스트 return,
# 후기남기기: 후기 양식 텍스트 return..
# 여기에 별점 버튼도 포함 !

