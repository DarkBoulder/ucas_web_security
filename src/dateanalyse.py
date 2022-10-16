import sys

# import ConfigParser
import time
import re
import csv
import pandas as pd
from pandas import Series, DataFrame


# 统计可能含日期的口令(连续数字位数大于等于4的)
def countProbPasswd(passwdList):
    df = []
    for i in range(len(passwdList)):
        passwd = str(passwdList[i])
        struc = ""
        for ch in passwd:
            if ch.isdigit():
                struc += 'D'
            elif ch.isalpha():
                struc += 'L'
            else:
                struc += 'S'

        char = struc[0]
        c = 1
        stri = struc[1:]
        res = ''
        for j in stri:
            if j == char:
                c += 1
            else:
                res += char
                res += str(c)
                char = j
                c = 1
        res += char
        res += str(c)

        # r'D[4-9]|D\d{2}'
        if re.search(r'D[4-9]|D\d{2}', res):
            df.append(passwd)

    return df


# 统计含数字日期的口令
def analysisDate(data, savepath, dataname):
    datePasswd = {'yyyy': 0, 'yyyymm': 0, 'yyyymmdd': 0, 'mmddyyyy': 0, 'ddmmyyyy': 0, 'yymmdd': 0, 'mmddyy': 0,
                  'ddmmyy': 0, 'mmdd': 0}
    for i in data:
        # yyyy 1700-2200
        if re.search(r'1[7-9]\d{2}|2[0-1]\d{2}', i):
            datePasswd['yyyy'] += 1
        # yyyy-mm
        if re.search(r'(1[7-9]\d{2}|2[0-1]\d{2})(0[1-9]|1[0-2])', i):
            datePasswd['yyyymm'] += 1
        # yyyy-mm-dd
        if re.search(r'(1[7-9]\d{2}|2[0-1]\d{2})(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])', i):
            datePasswd['yyyymmdd'] += 1
        # mm-dd-yyyy
        if re.search(r'(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])(1[7-9]\d{2}|2[0-1]\d{2})', i):
            datePasswd['mmddyyyy'] += 1
        # dd-mm-yyyy
        if re.search(r'(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])(1[7-9]\d{2}|2[0-1]\d{2})', i):
            datePasswd['ddmmyyyy'] += 1
        # yy-mm-dd
        if re.search(r'[0-9][0-9](0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])', i):
            datePasswd['yymmdd'] += 1
        # mm-dd-yy
        if re.search(r'(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])[0-9][0-9]', i):
            datePasswd['mmddyy'] += 1
        # dd-mm-yy
        if re.search(r'(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9][0-9]', i):
            datePasswd['ddmmyy'] += 1
        # mm-dd
        if re.search(r'(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])', i):
            datePasswd['mmdd'] += 1
    print('---------[' + dataname + ']date analyse------------')
    print(datePasswd)
    print('--------------------------------------------------')
    with open(savepath + "口令日期分析(统计)_{}.csv".format(dataname), 'w', encoding='utf-8-sig', newline='') as f:
        csv_writer = csv.writer(f)
        for ele in datePasswd.items():
            csv_writer.writerow([ele[0], ele[1]])


# 含英文日期的口令
def analysisEnDate(data, savepath, dataname):
    dic = ['Jan', 'January', 'Feb', 'February', 'Mar', 'March', 'Apr', 'April',
           'May', 'Jun', 'June', 'Jul', 'July', 'Aug', 'August', 'Sep', 'September',
           'Oct', 'October', 'Nov', 'November', 'Dec', 'December']
    lis = []
    for line in data:
        for i in dic:
            if i in str(line):
                lis.append(str(line))
    pd.Series(lis).to_csv(savepath + '口令日期分析(含英文日期)_' + dataname + '.csv')
    print("English password num:" + str(len(lis)))
    print('--------------------------------------------------')


# 只含日期密码的口令
def analysisDateOnly(data, savepath, dataname):
    lis = []
    for line in data:
        if re.match(r'\d+$', line):
            if re.match(r'1[7-9]\d{2}|2[0-1]\d{2}$', line):
                lis.append(line)
            elif re.match(r'(1[7-9]\d{2}|2[0-1]\d{2})(0[1-9]|1[0-2])$', line):
                lis.append(line)
            elif re.match(r'(1[7-9]\d{2}|2[0-1]\d{2})(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])$', line):
                lis.append(line)
            elif re.match(r'(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])$', line):
                lis.append(line)
    pd.Series(lis).to_csv(savepath + '口令日期分析(只含数字日期)_' + dataname + '.csv')


def AnalyseAndSave_yahoo(path, savepath, dataname):
    # 读取passwd
    # data = pd.read_csv(path + dataname + '.csv')
    # datapath = path + dataname + '.csv'
    # print(datapath)
    # print(path + dataname + '.csv')
    # print('./data/csdn.csv')
    # data = pd.read_csv('./data/csdn.csv')

    data = pd.read_csv('./data/yahoo.csv')
    passwdList = pd.Series(data['@fl!pm0de@'].values)
    # 读口令结构文件
    lis = countProbPasswd(passwdList)
    # 分析只含数字日期的口令并输出一个onlydate_passwd.csv
    analysisDateOnly(lis, savepath, dataname)
    # 分析含数字日期的口令，打印各日期格式的个数
    analysisDate(lis, savepath, dataname)
    # 分析含英文日期的口令，打印个数并输出一个Englishdate_passwd.csv
    analysisEnDate(lis, savepath, dataname)


def AnalyseAndSave_csdn(path, savepath, dataname):
    # 读取passwd
    # data = pd.read_csv(path + dataname + '.csv')
    # datapath = path + dataname + '.csv'
    # print(datapath)
    # print(path + dataname + '.csv')
    # print('./data/csdn.csv')
    # data = pd.read_csv('./data/csdn.csv')

    data = pd.read_csv('./data/csdn.csv')
    passwdList = pd.Series(data['12344321'].values)
    # 读口令结构文件
    lis = countProbPasswd(passwdList)
    # 分析只含数字日期的口令并输出一个onlydate_passwd.csv
    analysisDateOnly(lis, savepath, dataname)
    # 分析含数字日期的口令，打印各日期格式的个数
    analysisDate(lis, savepath, dataname)
    # 分析含英文日期的口令，打印个数并输出一个Englishdate_passwd.csv
    analysisEnDate(lis, savepath, dataname)


def DateAnalyse(path, savepath):
    AnalyseAndSave_yahoo(path, savepath, 'yahoo')
    AnalyseAndSave_csdn(path, savepath, 'csdn')
