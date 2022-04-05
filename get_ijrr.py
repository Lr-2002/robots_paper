import pandas as pd
"""
    how to easy get ijrr paper
    1. go to ijrr 
    2. search 'legged'
    3. select all 
    4. cite them
    5. download
    6. use this script to get abstract


"""

if __name__=='__main__':
    with open('./sage.ris','r') as f:
        lines = f.readlines()
    abstract = []
    name = []
    date = []
    doi = []
    for line in lines:
        line = line.strip()
        if 'N2' in line:
            abstract.append(line.split('-')[-1])
        elif 'PY' in line:
            date.append(line.split('-')[1])
        elif 'T1' in line:
            name.append(line.split('-')[-1])
        elif 'DO' in line:
            doi.append(line.split('-')[-1])
    
    print(len(abstract), len(name), len(date), len(doi))

    table = pd.DataFrame({'name':name, 'date':date, 'abstract':abstract, 'doi':doi}).to_csv('./sage.csv', index=False)