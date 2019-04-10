import vk_api
import os
import random

def ping(target:str):
    if os.system("ping -q -c 10 " + target +">>/dev/null") == 0:
        print(target + " is Up")
    else:
        print(target + " is down")
        bot = vk_api.VkApi(token="ff37122dadc19fe93680a55ec5a8dd09c7babcd7864b4657aa5fe47cc8eec7da3fbf48fffca6e388d534f")
        bot._auth_token()
        bot.method("messages.send",{"peer_id": 160500068, "random_id" : random.randint(1, 1000),"message": (target + " is down")})

def main():
    ping("drujite.ru")
    ping("shtormgrad.com")
    ping("shtormgrad.ru")
    #ping("misroka.ru")

main()