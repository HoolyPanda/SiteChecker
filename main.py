import vk_api
import os
import random
import time
import Farseer

def ping(target:str):
    a = os.system("nmap -sn -PS " + "192.168.0.4 | grep \"Host is up\"")
    if os.system("nmap -sn -PS " + target.replace('\n',"") + " | grep \"Host is up\"") == 0:
        print("======================================  " + target.replace('\n', "") + " is Up")
    else:
        print(target + " is down")
        bot = vk_api.VkApi(token=open("token", "r").readline())
        bot._auth_token()
        bot.method("messages.send",{"peer_id": 160500068, "random_id" : random.randint(1, 1000),"message": (target.replace('\n', "") + " is down")})

def main():
    i = 0
    Farseer.SpawnConfig("SiteChecker")
    while True:
        for line in open("config", "r"):
            if line != "":
                ping(line)
        i += 1
        if i == 12:
            bot = vk_api.VkApi(token=open("token", "r").readline())
            bot._auth_token()
            bot.method("messages.send",{"peer_id": 160500068, "random_id" : random.randint(1, 1000),"message": ("Бот все еще в сети")})
            i = 0
        time.sleep(3600)
main()