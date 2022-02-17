import vk_api
import parse as p
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import time
from datetime import datetime


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': get_random_id()})


token = 'Ваш токен вк апи'
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

hour = 3600

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.from_user:
            try:
                data = p.get_data()
                write_msg(event.user_id, "Данные за " + str(datetime.now()))
                for item in data:
                    write_msg(event.user_id, item[0])
                    msg = '№ | Балл | ФИО | Приоритет | Согласие на другие напр-я \n'
                    for index, string in enumerate(item[1], 1):
                        if string[1] != 'Ваше ФИО':
                            msg += '{0} {1} {2} {3} {4}\n'.format(str(index), string[0], string[1], string[2], string[3])
                        else:
                            msg += '{0} {1} {2} {3} {4}\n'.format(str(index), string[0], string[1], string[2], string[3])
                            break
                    write_msg(event.user_id, msg)
            except Exception:
                write_msg(event.user_id, p.error_msg)
            write_msg(event.user_id, "конец сообщения")
            time.sleep(hour * 4)
