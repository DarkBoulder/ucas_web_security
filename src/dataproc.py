import csv


def DataProcess(path):
    """
    Convert database to .csv
    :param path: folder file of databases
    :return:
    """

    with open(path + 'plaintxt_yahoo.txt', 'r', encoding='utf8') as f1, \
            open(path + 'yahoo.csv', 'w', encoding='utf-8-sig', newline='') as f2:
        csv_writer = csv.writer(f2)
        cur_line_num = 0
        first_line_num = 3073
        for line in f1.readlines():
            cur_line_num += 1
            if cur_line_num >= first_line_num:
                line_data = line.strip().split(':')
                if len(line_data) >= 3:
                    csv_writer.writerow([line_data[2]])
    print('Yahoo data processed!')
    with open(path + 'www.csdn.net.sql', 'r', encoding='utf8') as f1, \
            open(path + 'csdn.csv', 'w', encoding='utf-8-sig', newline='') as f2:
        csv_writer = csv.writer(f2)
        for line in f1.readlines():
            csv_writer.writerow([line.strip().split('#')[1].strip()])
    print('CSDN data processed!')


if __name__ == '__main__':
    pass
