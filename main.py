import vk_api
import os
import random
import time
import Farseer
import requests
import knocker

Knocker = knocker.Knocker(token= open('./token.cred', 'r').readline())

def ping(target:str):
    req = requests.get('https://' + target.replace('\n', '') + '/', verify= False)
    if req.status_code == 200:
        print("======================================  " + target.replace('\n', "") + " is Up")
    else:
        msg = target.replace('\n', '') + f' is down, code: {str(req.status_code)}'
        print(msg)
        bot = vk_api.VkApi(token=open("./token.cred", "r").readline())
        bot._auth_token()
        for line in open('./peers.cred', 'r').readlines():
            try:
                Knocker.SendMsg(messageText= msg, peerId= int(line))
            except Exception as e:
                print(str(e))
                pass
        # bot.method("messages.send",{"peer_id": 160500068, "random_id" : random.randint(1, 1000),"message": msg})

def main():
    i = 0
    Farseer.SpawnConfig(name = "SiteChecker", peerId = 160500068)
    while True:
        for line in open("config.config", "r"):
            if line != "":
                ping(line)
        i += 1
        if i == 12:
            Knocker.SendMsg(messageText= 'Бот все еще в сети', peerId= 160500068)
            i = 0
        time.sleep(3600)
main()