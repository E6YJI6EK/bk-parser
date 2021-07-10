from bs4 import BeautifulSoup as bs
import requests

ivcht_domain = 'https://abitur.sstu.ru/vpo/direction/2021/66/b/o/b'
ifst_domain = 'https://abitur.sstu.ru/vpo/direction/2021/68/b/o/b'
pinf_domain = 'https://abitur.sstu.ru/vpo/direction/2021/70/b/o/b'
pinzh_domain = 'https://abitur.sstu.ru/vpo/direction/2021/71/b/o/b'


def parse_data(url):
    page = requests.get(url)
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


def output():
    for index, item in enumerate(sorted(parse_data(ivcht_domain), reverse=True), 1):
        yield index, item[0], item[1], item[2], item[3]

# for i in output():
#     print(i)
