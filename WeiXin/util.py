import hashlib
import json
import xml.etree.cElementTree as ET
from . import config
import requests
def check(token, timestamp, nonce, signature):
    params = [token, timestamp, nonce]
    params.sort()
    target = ""
    for str in params:
        target += str
    #sha1加密
    target_sha1 = hashlib.sha1(target.encode("utf-8"))
    return target_sha1.hexdigest() == signature

def getAccessToken():
    url = config.TOKEN_URL.replace("APPID", config.APPID).replace("APPSECRET", config.APPSECRET)
    res = requests.get(url)
    return json.loads(res.text)
def createButton(accessToken):
    btn = dict()
    btn1 = dict()
    btn2 = dict()
    btnArr = list()
    btn1["type"] = "view"
    btn1["name"] = "baidu"
    btn1["url"] = "http://www.soso.com/"
    btn1["key"] = "V1001_TODAY_MUSIC"
    btn2["type"] = "view"
    btn2["name"] = "hupu"
    btn2["url"] = "http://bbs.hupu.com/bxj"
    btn2["key"] = "V1001_TODAY_MUSIt"
    btnArr.append(btn1)
    btnArr.append(btn2)
    btn["button"] = btnArr
    url = config.CREATE_BUTTON_URL.replace("ACCESS_TOKEN", accessToken.getToken())
    res = requests.post(url, json.dumps(btn))
    print(accessToken.getToken())
    print(res.text)

def parseXml(xmlStr):
    root = ET.fromstring(xmlStr)
    res = dict()
    for child in root:
        res[child.tag] = child.text
    return  res

def getTextMessageXml(mesDict):
    xmlStr = f"<xml><ToUserName><![CDATA[{mesDict['ToUserName']}]]></ToUserName><FromUserName><![CDATA[{mesDict['FromUserName']}]]></FromUserName><CreateTime>{mesDict['CreateTime']}</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[{mesDict['Content']}]]></Content></xml>"
    return xmlStr