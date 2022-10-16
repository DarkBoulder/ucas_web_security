# 键盘密码模式分析
import pandas as pd

# 所有可能的键盘密码序列
keyboard_pass1 = '1234567890qwertyuiopasdfghjkl;zxcvbnm,./'
keyboard_pass2 = '1234567890poiuytrewqasdfghjkl;/.,mnbvcxz'

keyboard_pass3 = '1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik,9ol.0p;/'
keyboard_pass4 = '1qazxsw23edcvfr45tgbnhy67ujm,ki89ol./;p0'

keyboard_pass5 = 'zaq1xsw2cde3vfr4bgt5nhy6mju7,ki8.lo9/;p0'
keyboard_pass6 = 'zaq12wsxcde34rfvbgt56yhnmju78ik,.lo90p;/'

keyboard_pass7 = '0987654321poiuytrewq;lkjhgfdsa/.,mnbvcxz'
keyboard_pass8 = '0987654321qwertyuioplkjhgfdsazxcvbnm,./'

keyboard_pass9 = 'qazwsxedcrfvtgbyhnujmik,ol.p;/'
keyboard_pass10 = 'qazxswedcvfrtgbnhyujm,kiol./;p'

keyboard_pass11 = 'zaqxswcdevfrbgtnhymju,ki.lo/;p'
keyboard_pass12 = 'zaqwsxcderfvbgtyhnmjuik,.lop;/'

keyboard_pass_all = keyboard_pass1 + keyboard_pass2 + keyboard_pass3 + keyboard_pass4 + keyboard_pass5 + keyboard_pass6 + keyboard_pass7 + keyboard_pass8 + keyboard_pass9 + keyboard_pass10 + keyboard_pass11


def Check_Keyboard_Password(passwdList, count):
    output = dict()

    for single_data in passwdList.values:
        # 将密码全部转换为字符串
        single_data = str(single_data)

        if single_data in keyboard_pass_all and len(single_data) > 1:
            # 如果是键盘密码，count +1
            count = count + 1

            if single_data in output:
                # 密码之前出现过，只增加数量
                output[single_data] = output[single_data] + 1
            else:
                # 密码没出现过，加入output
                output[single_data] = 1
    return output, count


def Probability(output, count):
    # turn output dict to Series
    output = pd.Series(output)
    # 降序排列
    output = output.sort_values(ascending=False)
    # turn Series to Dataframe
    df = pd.DataFrame({'password': output.index, 'numbers': output.values, 'probability': None})
    # 计算可能性
    index = df.index
    for index in index:
        df.loc[index, 'probability'] = str(float(df.loc[index, 'numbers']) / count).format(':.8f')
    return df


def AnalyseAndSave_yahoo(path, savepath, dataname):
    yahoo_path = path + 'yahoo.csv'
    data = pd.read_csv(yahoo_path)
    yahoo_psd_list = pd.Series(data['@fl!pm0de@'].values)

    # 统计yahoo中出现的键盘密码次数
    yahoo_output, yahoo_count = Check_Keyboard_Password(yahoo_psd_list, 0)

    # 计算可能性并按照降序排列
    df_yahoo = Probability(yahoo_output, yahoo_count)

    # 保存到csv文件
    df_yahoo.to_csv(savepath + '口令键盘分析_' + dataname + '.csv', columns=['password', 'numbers', 'probability'])


def AnalyseAndSave_csdn(path, savepath, dataname):
    csdn_path = path + 'csdn.csv'
    data = pd.read_csv(csdn_path)
    csdn_psd_list = pd.Series(data['12344321'].values)

    # 统计csdn中出现的键盘密码次数
    csdn_output, csdn_count = Check_Keyboard_Password(csdn_psd_list, 0)

    # 计算可能性并按照降序排列
    df_csdn = Probability(csdn_output, csdn_count)

    # 保存到csv文件
    df_csdn.to_csv(savepath + '口令键盘分析_' + dataname + '.csv', columns=['password', 'numbers', 'probability'])


def KeyboardAnalyse(path, savepath):
    AnalyseAndSave_yahoo(path, savepath, 'yahoo')
    AnalyseAndSave_csdn(path, savepath, 'csdn')
