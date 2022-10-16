import pandas as pd
import csv


def evaluate(pwd_generate, pwd_origin):
    length = 0
    accuracy = 0
    pwd_generate_set = set(pwd_generate)

    for i in range(len(pwd_origin)):
        if i % 10000 == 0:
            print('process: {}/{}'.format(i, len(pwd_origin)))

        if pwd_origin[i] in pwd_generate_set:
            accuracy += 1
            length += pwd_generate.index(pwd_origin[i])
        else:
            length += len(pwd_generate)

        # for j in range(len(df1_generate)):
        #     flag = 0
        #     if df2_original.iloc[i, 0] == df1_generate['passwd'][j]:  # 猜对了
        #         accuracy += 1
        #         length += j
        #         flag = 1
        #         break
        #     # else:
        #     #     length += 1
        #     #     continue
        #     if j == (len(df1_generate) - 1) and flag == 0:  # 未猜中
        #         length += j

                # if df1_generate['passwd'][i] in yahoo_dict_original.iloc[:, 0]:
        #     accuracy += 1
    return accuracy / len(pwd_origin), length / len(pwd_origin)


def dataEvaluate(datapath, respath, dataname):
    # dict_original = pd.read_csv(datapath + '{}.csv'.format(dataname))
    # dict_generate = pd.read_csv(respath + 'pcfg_{}.csv'.format(dataname))

    pwd_origin = []
    with open(datapath + '{}.csv'.format(dataname), 'r', encoding='utf-8-sig') as f1:
        for row in csv.reader(f1):
            pwd_origin.append(row[0])

    pwd_generate = []
    with open(respath + 'pcfg_{}.csv'.format(dataname), 'r', encoding='utf-8-sig') as f1:
        for row in csv.reader(f1):
            pwd_generate.append(row[0])
    pwd_generate.pop(0)

    print('evaluating {} data.'.format(dataname))
    Accuracy, avg_length = evaluate(pwd_generate, pwd_origin)

    with open(respath + "口令字典准确度与平均猜测长度_{}.csv".format(dataname), 'w', encoding='utf-8-sig', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['数据来源', '准确度', '平均猜测长度'])
        csv_writer.writerow([dataname, '{:.3f}%'.format(Accuracy * 100), '{:.3f}'.format(avg_length)])


def pcfgEvaluate(datapath, respath):
    dataEvaluate(datapath, respath, 'yahoo')
    dataEvaluate(datapath, respath, 'csdn')




