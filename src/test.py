from dataclasses import dataclass
# import pandas as pd
# datas = pd.read_csv('./data/csdn.csv')
import csv

# path = './data/'
# dataname = 'yahoo'
# passwdList = pd.Series(datas['12344321'].values)

if __name__ == '__main__':
    dic = {'a': 12, 'b': 13}
    with open("test.csv", 'w', encoding='utf-8-sig', newline='') as f:
        csv_writer = csv.writer(f)
        for ele in dic.items():
            csv_writer.writerow([ele[0], ele[1]])
