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

    return accuracy / len(pwd_origin), length / accuracy, \
           (length + len(pwd_generate) * (len(pwd_origin) - accuracy)) / len(pwd_origin)


def dataEvaluate(datapath, respath, dataname):
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
    Accuracy, avg_length, total_avg_length = evaluate(pwd_generate, pwd_origin)

    with open(respath + "口令字典准确度与平均猜测长度_{}.csv".format(dataname), 'w', encoding='utf-8-sig', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['数据来源', '准确度', '平均猜测长度（正确）', '平均猜测长度（总共）'])
        csv_writer.writerow([dataname, '{:.3f}%'.format(Accuracy * 100), '{:.3f}'.format(avg_length), '{:.3f}'.format(total_avg_length)])


def pcfgEvaluate(datapath, respath):
    dataEvaluate(datapath, respath, 'yahoo')
    dataEvaluate(datapath, respath, 'csdn')




