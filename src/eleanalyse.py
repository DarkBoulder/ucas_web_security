import csv

substr_dict = {}


def GetLetterType(letter):
    if isinstance(letter, str):
        if letter.isdigit():
            return 'D'
        elif letter.isalpha():
            return 'L'
        else:
            return 'S'


def PasswordAnalyse(pwd):
    global substr_dict
    res = ''
    substr = ''
    last_type = None
    last_cnt = 0

    if pwd == '':
        return res
    for i in range(len(pwd)):
        letter_type = GetLetterType(pwd[i])
        if letter_type == last_type:
            last_cnt += 1
            substr += pwd[i]
        elif last_type is not None:
            res += last_type
            res += str(last_cnt)
            last_type = letter_type
            last_cnt = 1
            substr_dict[substr] = substr_dict.get(substr, 0) + 1
            substr = pwd[i]
        else:
            last_type = letter_type
            last_cnt += 1
            substr += pwd[i]

    res += last_type
    res += str(last_cnt)
    substr_dict[substr] = substr_dict.get(substr, 0) + 1
    return res


def AnalyseAndSave(path, savepath, dataname):
    global substr_dict
    res_dict = {}
    substrres_dict = {}

    with open(path + dataname + '.csv', 'r', encoding='utf-8-sig') as f:
        for row in csv.reader(f):
            pwd = row[0]
            res = PasswordAnalyse(pwd)
            res_dict[res] = res_dict.get(res, 0) + 1
    sorted_dict = sorted(res_dict.items(), key=lambda x: x[1], reverse=True)

    total_cnt = 0
    for ele in sorted_dict:
        total_cnt += ele[1]

    for ele in substr_dict.items():
        pwd_type = GetLetterType(ele[0][0]) + str(len(ele[0]))
        if pwd_type in substrres_dict:
            substrres_dict[pwd_type].append('{}-{}'.format(ele[0], str(ele[1])))
        else:
            substrres_dict[pwd_type] = ['{}-{}'.format(ele[0], str(ele[1]))]

    with open(savepath + "口令结构频率分析_{}.csv".format(dataname), 'w', encoding='utf-8-sig', newline='') as f:
        csv_writer = csv.writer(f)
        for ele in sorted_dict:
            csv_writer.writerow([ele[0], ele[1], int(ele[1]) / total_cnt])
    print("口令结构频率分析_{}.csv generated.".format(dataname))

    with open(savepath + "口令结构子串统计分析_{}.csv".format(dataname), 'w', encoding='utf-8-sig', newline='') as f:
        csv_writer = csv.writer(f)
        for ele in substrres_dict.items():
            output_dict = [ele[0]] + ele[1]
            csv_writer.writerow(output_dict)
    print("口令结构子串统计分析_{}.csv generated.".format(dataname))
    substr_dict = {}


def ElementAnalyse(path, savepath):
    AnalyseAndSave(path, savepath, 'yahoo')
    AnalyseAndSave(path, savepath, 'csdn')


if __name__ == '__main__':
    print(PasswordAnalyse('电子技术基础数字部分第五版'))
