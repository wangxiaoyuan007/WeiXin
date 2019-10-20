from . import util
import time
class AcccessToken:
    def __init__(self):
        self.accessToken = ""
        self.expireTime = 0

    def getToken(self):
        if self.accessToken == "" or self.expireTime < int(time.time()):
            print("new")
            res = util.getAccessToken()
            self.accessToken = res["access_token"]
            self.expireTime = int(time.time()) + int(res["expires_in"])
        return self.accessToken