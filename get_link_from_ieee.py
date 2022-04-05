from selenium import webdriver
import urllib
import pandas as pd
import logging
from selenium.webdriver.common.by import By
from tqdm import trange, tqdm
import threading
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def save_html(filename, file_content):
    with open(filename+'.html', 'x', encoding='utf-8') as f:
        f.write(file_content)


df = pd.read_csv('./tro_name.csv')
table = df.values
option = webdriver.ChromeOptions()
option.add_argument('headless')
name = table[:,1]
# print('your total file number is', len(name))
logging.info('your total file number is %d', len(name))
browser = webdriver.Chrome(options=option)
warning = []
note_list = []
with tqdm(total=len(name)) as pbar:
    for filename in name:
        
        # filename = 'The Dynamic Effect of Mechanical Losses of Transmissions on the Equations of Motion of Legged Robots'
        filename = urllib.parse.quote(filename)
        search = 'https://ieeexplore.ieee.org/search/searchresult.jsp?'+'newsearch=true&queryText='+filename

        xpath = '/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/main/div[2]/div[2]/xpl-results-list/div[3]/xpl-results-item/div[1]/div[1]/div[2]/h2/a'
        browser.get(search)
        try:
            # element = browser.find_element(By.XPATH, xpath)
            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            temp = element.get_attribute('href')
            note_list.append(temp)
        except:
            filename = urllib.parse.unquote(filename)
            logging.warning('%s could not be processed by me', filename)
            warning.append(filename)
            note_list.append(0)
            continue
        pbar.update(1)
browser.quit()
pd.DataFrame({'name':name, 'note_list':note_list}).to_csv('./link_list.csv', index=False)
pd.DataFrame({'name':warning}).to_csv('./warning.csv', index=False)
print('Total:', len(name), 'Deparced:', len(warning))