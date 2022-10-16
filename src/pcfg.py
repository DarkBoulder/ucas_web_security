import time
import re
import csv

import pandas as pd
from pandas import DataFrame

DIC_NUMS = 5000


class PCFG_gene:
    def __init__(self, structure_df, str_list):
        self.structure_df = structure_df
        self.str_list = str_list

    def PCFG_Pre(self):
        stru_dic = {}
        stru_nums = {}
        for tmp_list in self.str_list:
            tmp_dict = {}
            sums = 0
            for i in range(1, len(tmp_list)):
                str_toparse = tmp_list[i]
                index = re.search(r'-\d+$', str_toparse).span()
                num = int(str_toparse[index[0] + 1:])
                sums += num
                tmp_dict[str_toparse[:index[0]]] = num
            stru_dic[tmp_list[0]] = tmp_dict
            stru_nums[tmp_list[0]] = sums
        return stru_dic, stru_nums

    def PCFG_gene_list(self, stru_dic, stru_nums, savepath, dataname):
        passwd_list = {}
        for i in range(len(self.structure_df)):
            passwd_list[self.structure_df.iloc[i][0]] = float(self.structure_df.iloc[i][2])
        result = {}
        cnum = 0

        for key in passwd_list.keys():
            cnum += 1
            parse_list = re.findall(r'[A-Z]\d+', str(key))
            final_freq = passwd_list[key]
            final_list = {'': final_freq}
            for sub_str in parse_list:
                if sub_str in stru_dic.keys():
                    lis = sorted(stru_dic[sub_str].items(), key=lambda item: item[1], reverse=True)
                    tmp_dic = {}
                    for j in range(int(passwd_list[key] * DIC_NUMS) + 1):  # 这里的长度选取有待商榷
                        if j < len(lis):
                            prob = lis[j][1] * 1.0 / stru_nums[sub_str]
                            for s in final_list.keys():
                                tmp_dic[lis[j][0] + s] = final_list[s] * prob
                    final_list = tmp_dic
            if final_list:
                result[key] = final_list
        result_list = {}
        for k in result.keys():
            for r in result[k].keys():
                result_list[r] = result[k][r]
        if sub_str in stru_dic.keys():
            res = sorted(result_list.items(), key=lambda item: item[1], reverse=True)
            df = DataFrame(columns=('passwd', 'prob'))
            for q in range(DIC_NUMS):
                df.loc[res[q][0]] = [res[q][0], res[q][1]]
            df.to_csv(savepath + 'pcfg_{}.csv'.format(dataname), index=False)


def pcfgAnalyse(path, savepath, dataname):
    time1 = time.time()

    # --------------------读文件模块--------------------#
    # 读取结构串文件
    structure_df = pd.read_csv(path + '口令结构频率分析_{}.csv'.format(dataname))
    csv_file = csv.reader(open(path + '口令结构子串统计分析_{}.csv'.format(dataname), 'r', encoding='utf-8-sig'))  # 子串频率

    str_list = []
    for i in csv_file:  # i = each line in csv = ['', '', ...]
        str_list.append(i)

    time2 = time.time()
    print('read file time : ', (time2 - time1))

    p = PCFG_gene(structure_df, str_list)
    stru_dic, stru_nums = p.PCFG_Pre()  # stru_dic = {'L2': {'fl': 48, 'pm': 33, 'de': 65, 'lb': 40}
    p.PCFG_gene_list(stru_dic, stru_nums, savepath, dataname)

    time3 = time.time()
    print('Analysis time : ', (time3 - time2))


def pcfgGenerate(path, savepath):
    # pcfgAnalyse(path, savepath, 'yahoo')
    pcfgAnalyse(path, savepath, 'csdn')

