import pandas as pd
import os
global end_list

def listt(name):
    a = pd.read_csv(name)

    table = a.values

    # print(table.shape[0])
    # b = [] 
    for i in range(table.shape[0]):
        # print(str(table[i][0]))
        if str(table[i][0]).lower().find('legged') != -1:
            end_list.append(table[i][0])
    return 1
if __name__ == '__main__':
    dir_list = os.listdir('./')
    end_list=[]
    for i in dir_list:
        if i.endswith('.csv'):
            listt(i)
    print(end_list)
    df = pd.DataFrame(end_list)
    df.to_csv('./end_list.csv')