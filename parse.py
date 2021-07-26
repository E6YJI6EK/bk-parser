from bs4 import BeautifulSoup as bs
import requests

ivcht_domain = 'https://abitur.sstu.ru/vpo/direction/2021/33/b/o/b'
ifst_domain = 'https://abitur.sstu.ru/vpo/direction/2021/35/b/o/b'
pinf_domain = 'https://abitur.sstu.ru/vpo/direction/2021/37/b/o/b'
pinzh_domain = 'https://abitur.sstu.ru/vpo/direction/2021/38/b/o/b'
domains = {'ИВЧТ': ivcht_domain, 'ИФСТ': ifst_domain, 'ПИНФ': pinf_domain, 'ПИНЖ': pinzh_domain}
error_msg = "Не могу сделать запрос на сервер"


def parse_data(url):
    page = requests.get(url)
    if page.status_code == 200:
        soup = bs(page.text, 'html.parser')
        table = bs(str(soup.find_all('div', attrs={'class': 'rasp-block'})[-1]), 'html.parser')
        tbody = table.find('tbody', attrs={'class': 'text-center'})
        data = bs(str(tbody), 'html.parser')
        trs = data.find_all('tr')
        lst = []
        for tr in trs:
            temp = bs(str(tr), 'html.parser').find_all('td')
            lst += [[temp[2].text.strip(),
                     temp[1].text.strip().replace('\r\n', '').split(
                         '                                                                                                                                                        ')[
                         0], temp[7].text.strip(), temp[8].text.strip()]]
        return lst
    else:
        return error_msg


def get_data():
    for key in domains.keys():
        data = parse_data(domains[key])
        if data != error_msg:
            yield key, sorted(data, reverse=True)
        else:
            return error_msg


# for i in get_data():
#     print(i)

