import pandas as pd


def txt2csv(txt_path, csv_path):
    '''
    txt文件转csv文件
    :param txt_path:
    :param csv_path:
    :return:
    '''
    # 读取数据
    data = pd.read_table(txt_path, sep='\t', error_bad_lines=False, header=None)

    # 写入csv
    data.to_csv(csv_path, index=False, header=False)


def list2csv(list_data, csv_path):
    '''
    list数据保存csv文件
    :param list_data:
    :param csv_path:
    :return:
    '''
    data = pd.DataFrame(data=list_data)
    data.to_csv(csv_path, index=False, header=False)

