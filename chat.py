import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

def main():
    replies = [ "ответ1", "ответ2", "ответ3" ]
    bot_session = vk_api.VkApi(token=token)
    bot_api = bot_session.get_api()
    while True:
        longpoll = VkBotLongPoll(bot_session, g_id)
        try:
            for event in longpoll.listen():
                print("got event")
                if event.type == VkBotEventType.MESSAGE_NEW:
                    print("message")
                    bot_api.messages.send(
                        random_id=random.getrandbits(32),
                        peer_id=event.obj.peer_id,
                        message=random.choice(replies)
                    )
        # ...
        except requests.exceptions.ReadTimeout as timeout:
            continue
if __name__ == '__main__':
    main()
