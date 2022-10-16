# 分析每一种纯口令结构最常用的十个口令以及他们的数量
import re
import pandas as pd
from pandas import Series, DataFrame

import csv


class Analysis(object):
    def __init__(self, passwdList):
        self.passwdList = passwdList

    # 统计纯数字和字母的口令数量
    def countDorL(self):
        # 统计总条数
        dic = {'L1': {}, 'L2': {}, 'L3': {}, 'L4': {}, 'L5': {}, 'L6': {}, 'L7': {}, 'L8': {}, 'L9': {}, 'L10': {},
               'L11': {}, 'L12': {}, 'L13': {}, 'L14': {}, 'L15': {}, 'L16': {}, 'L17': {}, 'L18': {}, 'L19': {},
               'L20': {}, 'L21': {},
               'S1': {}, 'S2': {}, 'S3': {}, 'S4': {}, 'S5': {}, 'S6': {}, 'S7': {}, 'S8': {}, 'S9': {}, 'S10': {},
               'S11': {}, 'S12': {}, 'S13': {}, 'S14': {}, 'S15': {}, 'S16': {}, 'S17': {}, 'S18': {}, 'S19': {},
               'S20': {}, 'S21': {},
               'D1': {}, 'D2': {}, 'D3': {}, 'D4': {}, 'D5': {}, 'D6': {}, 'D7': {}, 'D8': {}, 'D9': {}, 'D10': {},
               'D11': {}, 'D12': {}, 'D13': {}, 'D14': {}, 'D15': {}, 'D16': {}, 'D17': {}, 'D18': {}, 'D19': {},
               'D20': {}, 'D21': {}}
        df = DataFrame(columns=('structure', 'nums', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
        patternLetter = re.compile(r'[A-Za-z]+$')
        patternDigit = re.compile(r'\d+$')
        patternSig = re.compile(r'\W+$')
        for line in self.passwdList:
            line = str(line)
            l = ''
            if patternLetter.match(line):
                l = 'L' + str(len(line))
            elif patternDigit.match(line):
                l = 'D' + str(len(line))
            elif patternSig.match(line):
                l = 'S' + str(len(line))
            if l:
                if line in dic[l]:
                    dic[l][line] += 1
                else:
                    dic[l][line] = 1

        for tp in dic:
            every_dic = dic[tp]
            sums = sum(every_dic.get(x) for x in every_dic)
            rows = [tp, sums]
            every_dic = sorted(every_dic.items(), key=lambda x: x[1], reverse=True)
            if len(every_dic) > 10:
                for r in range(10):
                    rows.append(str(every_dic[r]))
            else:
                for r in range(len(every_dic)):
                    rows.append(str(every_dic[r][0]) + ' : ' + str(every_dic[r][1]))
                for r in range(10 - len(every_dic)):
                    rows.append(0)
            df.loc[tp] = rows
        df = df.sort_values(by='nums', ascending=False)
        return df


def AnalyseAndSave(path, savepath, dataname):
    # 读取文件
    data = pd.read_csv(path + dataname + '.csv')
    passwdList = pd.Series(data.values.ravel())

    ana = Analysis(passwdList)
    # 分析生成仅由字母/数字组成的口令数量, 以及每种结构频率TOP10的口令
    ana.countDorL().to_csv(savepath + '常用纯口令分析_' + dataname + '.csv', index=False)


def TopAnalyse(path, savepath):
    AnalyseAndSave(path, savepath, 'yahoo')
    AnalyseAndSave(path, savepath, 'csdn')


if __name__ == '__main__':
    print('')
