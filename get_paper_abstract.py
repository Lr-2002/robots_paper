from numpy import save
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd
from torch import abs_
def save_html(filename, file_content):
    with open(filename+'.html', 'x', encoding='utf-8') as f:
        f.write(file_content)


def get_data(url, header, save_htm=False):
    try:
        r = requests.get(url, headers=header)
        if r.status_code == 200:
            if save_htm:
                save_html('test', r.text)
            return r.text
        else:
            return None
    except Exception as e:
        print(e)
        return None

df = pd.read_csv('./link_list.csv')
table = df.values
name = table[:,1]
total = table[:, 0]
id_list = [int(x[-8:-1]) for x in name]

header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en,zh-CN;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,zh;q=0.6',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    'Cookie':'LT=XPLLG_XPL_2022_SUB_SignIn_Purchase; fp=5f4197044439aa368f9f7e063484f842; s_fid=261989FE85FF9A19-3F531D9CFD216ADC; cookieconsent_status=dismiss; WLSESSION=186802828.20480.0000; TS01b03060=012f3506236461d98235ee8dbb3a8a20cb6123ebbed9a95b5ac3f01cc15ef5ffbfe737fefa94b649fd7fce817ee7fb15f4e370ba39; JSESSIONID=vUrvfSGcRFBmsNvuah173YjS0Jmv-5V2Nac5LSwV4qK3GEOF9Kwm!-714980361; ipCheck=31.222.226.120; AMCVS_8E929CC25A1FB2B30A495C97@AdobeOrg=1; AMCV_8E929CC25A1FB2B30A495C97@AdobeOrg=1687686476|MCIDTS|19085|MCMID|51750564065909420302127967213884645380|MCAID|NONE|MCOPTOUT-1648997668s|NONE|vVersion|3.0.0; s_cc=true; utag_main=v_id:017fea74237e001361697e2e575705068002c06000bd0$_sn:4$_se:4$_ss:0$_st:1648992299982$vapi_domain:ieee.org$ses_id:1648990434791;exp-session$_pn:4;exp-session; s_sq=[[B]]',
    'Host':'ieeexplore.ieee.org',
    'Referer':'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=Learning a Centroidal Motion Planner for Legged Locomotion',
}

abs_list = []
print(len(id_list))
with tqdm(total=len(id_list)) as pbar:
    for i in id_list:
        link='https://ieeexplore.ieee.org/document/'+str(i)
        print(link)
        try:
            ieee_response = requests.get(url=link, headers=header)
            soup = BeautifulSoup(ieee_response.text, 'lxml')
            pattern = re.compile(r'xplGlobal.document.metadata=(.*?);', re.MULTILINE | re.DOTALL)
            get_data(link, header)
            script = soup.find('script', text=pattern)
            res_dic = pattern.search(script.text).group(1)
            try:
                json_data = json.loads(res_dic)
                abs_list.append(json_data['abstract'])
            except:
                abs_list.append('')
        except:
            abs_list.append(' ')
        
        pbar.update(1)

abs_dict = {'name':total, 'abs':abs_list, 'link':name}
df = pd.DataFrame(abs_dict).to_csv('abstract.csv', index=False)