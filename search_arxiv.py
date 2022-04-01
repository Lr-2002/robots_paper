from traceback import print_tb
import pandas as pd
import requests

df = pd.read_csv('./end_list.csv')

table = df.values

url = 'https://arxiv.org/search/'

data = {
    'size':50,
    'order':'-announced_date_first',
}

for i in range(table.shape[0]):
    name = table[i][1]
    name = name.replace(' ', '+')
    data['query'] = name
    r = requests.post(url, data=data)
    print(r)
