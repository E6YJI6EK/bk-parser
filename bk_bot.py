import vk_api
import parse as p
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import time
from datetime import datetime


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': get_random_id()})


token = '5aab5f0fd363d2e904c77896ed1861377251dc1c8f401defda9bd17ddcbc3ed7bf0f3b8d18c799f1cef6e'
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.from_user:
            request = event.text.upper().strip()
            print(request, event.user_id)
            data = p.parse_data(p.ivcht_domain)
            write_msg(event.user_id, "Данные за " + str(datetime.now()))
            result = 'ИВЧТ \n № | Балл | ФИО | Приоритет | Согласие на другие напр-я \n'
            for index, item in enumerate(sorted(data, reverse=True), 1):
                if item[1] != 'Нуржанов Айшат Бердагалиевич':
                    result += str(index) + ' ' + item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[3] + '\n'
                else:
                    result += str(index) + ' ' + item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[
                        3] + '\n' + "КОНЕЦ"
                    break
            write_msg(event.user_id, result)
            data = p.parse_data(p.ifst_domain)
            result = 'ИФСТ \n № | Балл | ФИО | Приоритет | Согласие на другие напр-я \n'
            for index, item in enumerate(sorted(data, reverse=True), 1):
                if item[1] != 'Нуржанов Айшат Бердагалиевич':
                    result += str(index) + ' ' + item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[3] + '\n'
                else:
                    result += str(index) + ' ' + item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[
                        3] + '\n' + "КОНЕЦ"
                    break
            write_msg(event.user_id, result)
            data = p.parse_data(p.pinf_domain)
            result = 'ПИНФ \n № | Балл | ФИО | Приоритет | Согласие на другие напр-я \n'
            for index, item in enumerate(sorted(data, reverse=True), 1):
                if item[1] != 'Нуржанов Айшат Бердагалиевич':
                    result += str(index) + ' ' + item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[3] + '\n'
                else:
                    result += str(index) + ' ' + item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[
                        3] + '\n' + "КОНЕЦ"
                    break
            write_msg(event.user_id, result)
            data = p.parse_data(p.pinzh_domain)
            result = 'ПИНЖ \n № | Балл | ФИО | Приоритет | Согласие на другие напр-я \n'
            for index, item in enumerate(sorted(data, reverse=True), 1):
                if item[1] != 'Нуржанов Айшат Бердагалиевич':
                    result += str(index) + ' ' + item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[3] + '\n'
                else:
                    result += str(index) + ' ' + item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[
                        3] + '\n' + "КОНЕЦ"
                    break
            write_msg(event.user_id, result)
            print("конец сообщения")
            time.sleep(3600)
