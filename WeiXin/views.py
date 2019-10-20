from flask import Flask, request
from . import util
from . import config
import time
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index():
    util.getAccessToken()
    return "hello world"

@app.route("/wx", methods=['POST'])
def wx():
    # signature = request.args.get("signature")
    # echostr = request.args.get("echostr")
    # timestamp = request.args.get("timestamp")
    # nonce = request.args.get("nonce")
    # if(util.check(config.token, timestamp, nonce, signature)):
    #     return echostr
    # else:
    #     return "failed"
    data = request.get_data()
    receiveMesMap = util.parseXml(str(data, encoding="utf-8"))
    sendMesMap = dict()
    sendMesMap['ToUserName'] = receiveMesMap['FromUserName']
    sendMesMap['FromUserName'] = config.USER_NAME
    sendMesMap['CreateTime'] = int(time.time())
    sendMesMap['Content'] = "你好，你干嘛发：" + receiveMesMap['Content']
    mes = util.getTextMessageXml(sendMesMap)
    print(mes)
    return mes

