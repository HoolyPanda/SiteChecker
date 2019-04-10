import vk_api
import os
import random
import time

def ping(target:str):
    if os.system("ping -q -c 10 " + target +" > /dev/null") == 0:
        print(target.replace('\n', "") + " is Up")
    else:
        print(target + " is down")
        bot = vk_api.VkApi(token=open("token", "r").readline())
        bot._auth_token()
        bot.method("messages.send",{"peer_id": 160500068, "random_id" : random.randint(1, 1000),"message": (target.replace('\n', "") + " is down")})

def main():
    while True:
        for line in open("config", "r"):
            if line != "":
                ping(line)
        time.sleep(3600)
main()