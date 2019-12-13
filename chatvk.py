g_id = "айди группы"

token = "токен группы"
import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

def main():
    privar = [ "Ghbdtn", "Здарова", "хай","привет", "дарова", "привет", ]
    bot_session = vk_api.VkApi(token=token)
    bot_api = bot_session.get_api()
    while True:
        longpoll = VkBotLongPoll(bot_session, g_id)
        try:
            for event in longpoll.listen():

                if event.type == VkBotEventType.MESSAGE_NEW:
                    if event.object.text in privar:
                        print(event.object.text)
                        bot_api.messages.send(
                            random_id=random.getrandbits(32),
                            peer_id=event.obj.peer_id,
                            message=random.choice(privar)
                        )
                    if event.object.text.find(']') != -1:
                        if event.object.text[event.object.text.find(']')+2:] in privar:
                            print(event.object.text)
                            bot_api.messages.send(
                                random_id=random.getrandbits(32),
                                peer_id=event.obj.peer_id,
                                message=random.choice(privar)
                            )





        except requests.exceptions.ReadTimeout as timeout:
            continue
if __name__ == '__main__':
    main()