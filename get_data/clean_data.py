import csv
import pandas as pd

# 文件路径
row_path = "D://PYTHON//data//all_data.csv"
train_1_path = "D://PYTHON//data//train_data_1.csv"
train_2_path = "D://PYTHON//data//train_data_2.csv"
train_3_path = "D://PYTHON//data//train_data_3.csv"
learn_path = "D://PYTHON//data//learn_path.csv"
test_path = "D://PYTHON//data//test_path.csv"
test_1_path = "D://PYTHON//data//test_data.csv"

MAX_COUNT = 1000000

data = pd.read_csv(row_path, encoding='gbk', nrows=MAX_COUNT, header=None)

for i in range(len(data)):
    # print(data[0][i])
    if data[0][i] == "售前售后":
        print("售前售后")
        data.drop([i],inplace=True)

# data.to_csv(train_3_path, index=False, header=False)
print(data)
