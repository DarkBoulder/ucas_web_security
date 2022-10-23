import matplotlib.pyplot as plt


def DrawBarChart(x, y, xlable, ylable, title, savepath, figsize=(10, 4), barwidth=0.4):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=figsize)
    plt.bar(x, y, width=barwidth)

    plt.xticks(range(max(x) + 1))
    plt.xlabel(xlable)
    plt.ylabel(ylable)
    plt.title(title)
    plt.legend(loc='best')
    # plt.show()
    plt.savefig(savepath)
