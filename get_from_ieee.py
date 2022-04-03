from webbrowser import Chrome
from selenium import webdriver
import urllib
import pandas as pd
from selenium.webdriver.common.by import By
from tqdm import trange, tqdm
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
def save_html(filename, file_content):
    with open(filename+'.html', 'x', encoding='utf-8') as f:
        # print(file_content)
        f.write(file_content)

# def get_data(url):
#     print(url)
#     try:
#         r = requests.get(url)
#         if r.status_code == 200:
            
#             # save_html(data['queryText'], r.text)
#             return r.text
#         else:
#             return None
#     except Exception as e:
#         print(e)
#         return None
df = pd.read_csv('./end_list.csv')
table = df.values
option = webdriver.ChromeOptions()
option.add_argument('headless')
name = table[:,1]
print(name) 
browser = webdriver.Chrome(options=option)

note_list = []
with tqdm(total=len(name)) as pbar:
    for filename in name:
        # filename = 'The Dynamic Effect of Mechanical Losses of Transmissions on the Equations of Motion of Legged Robots'
        filename = urllib.parse.quote(filename)
        search = 'https://ieeexplore.ieee.org/search/searchresult.jsp?'+'newsearch=true&queryText='+filename
        # search = 'https://www.baidu.com'

        # get_data(search)

        xpath = '/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/main/div[2]/div[2]/xpl-results-list/div[3]/xpl-results-item/div[1]/div[1]/div[2]/h2/a'
        browser.get(search)
        try:
            # element = browser.find_element(By.XPATH, xpath)
            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            temp = element.get_attribute('href')
            print(temp)
            note_list.append(temp)
        except:
            note_list.append(0)
            continue
        pbar.update(1)
browser.quit()
pd.DataFrame({'name':name, 'note_list':note_list}).to_csv('./note_list_1.csv', index=False)