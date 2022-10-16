import csv


def AnalyseAndSave(path, savepath, dataname):
    len_dict = {}
    with open(path + dataname + '.csv', 'r', encoding='utf-8-sig') as f1:
        for row in csv.reader(f1):
            pwdlen = len(row[0])
            len_dict[pwdlen] = len_dict.get(pwdlen, 0) + 1
    sorted_dict = sorted(len_dict.items())
    with open(savepath + '口令长度分析_{}.csv'.format(dataname), 'w', encoding='utf-8-sig', newline='') as f:
        csv_writer = csv.writer(f)
        for ele in sorted_dict:
            csv_writer.writerow([ele[0], ele[1]])
    print('口令长度分析_{}.csv generated.'.format(dataname))


def LengthAnalyse(path, savepath):
    AnalyseAndSave(path, savepath, 'yahoo')
    AnalyseAndSave(path, savepath, 'csdn')


