import pandas as pd
import requests
from lxml import etree

def save_html(filename, file_content):
    with open(filename+'.html', 'wb') as f:
        f.write(file_content)


df = pd.read_csv('./end_list.csv')

table = df.values

url = 'https://arxiv.org/search/'

data = {
    'query':'',
    'searchtype': 'all',
    'abstracts': 'show',
    'order':'-announced_date_first',
    'size':50,
    
}

for i in range(table.shape[0]):
    name = table[i][1]
    name = 'Learning a Centroidal Motion Planner for Legged Locomotion'
    name = name.replace(' ', '+')
    data['query'] = name
    print(data)
    r = requests.get(url, data=data)
    html = r.text
    save_html(name, html)
    print(html)
    try:
        selector = etree.HTML(html)
        links = selector.xpath('//*[@id="main-container"]/div[2]/ol/li/div/p/a')
        print(links)
    except:
        print('sorry')
