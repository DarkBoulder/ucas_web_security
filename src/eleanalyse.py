import csv


def GetLetterType(letter):
    if isinstance(letter, str):
        if letter.isdigit():
            return 'D'
        elif letter.isalpha():
            return 'L'
        else:
            return 'S'


def PasswordAnalyse(pwd):
    res = ''
    last_type = None
    last_cnt = 0
    if pwd == '':
        return res
    for i in range(len(pwd)):
        letter_type = GetLetterType(pwd[i])
        if letter_type == last_type:
            last_cnt += 1
        elif last_type is not None:
            res += last_type
            res += str(last_cnt)
            last_type = letter_type
            last_cnt = 1
        else:
            last_type = letter_type
            last_cnt += 1
    res += last_type
    res += str(last_cnt)
    return res


def AnalyseAndSave(path, savepath, dataname):
    res_dict = {}
    with open(path + dataname + '.csv', 'r', encoding='utf8') as f:
        for row in csv.reader(f):
            pwd = row[0]
            res = PasswordAnalyse(pwd)
            res_dict[res] = res_dict.get(res, 0) + 1
    sorted_dict = sorted(res_dict.items(), key=lambda x: x[1], reverse=True)
    with open(savepath + "口令结构分析_{}.csv".format(dataname), 'w', encoding='utf8', newline='') as f:
        csv_writer = csv.writer(f)
        for ele in sorted_dict:
            csv_writer.writerow([ele[0], ele[1]])
    print("口令结构分析_{}.csv generated.".format(dataname))


def ElementAnalyse(path, savepath):
    AnalyseAndSave(path, savepath, 'yahoo')
    AnalyseAndSave(path, savepath, 'csdn')


if __name__ == '__main__':
    print(PasswordAnalyse(''))

