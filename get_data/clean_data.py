import csv
import pandas as pd

# 文件路径
row_path = "D://PYTHON//word2vec//data//all_data.csv"
train_1_path = "D://PYTHON//word2vec//data//train_data_1.csv"
train_2_path = "D://PYTHON//word2vec//data//train_data_2.csv"
learn_path = "D://PYTHON//word2vec//data//learn_path.csv"
test_path = "D://PYTHON//word2vec//data//test_path.csv"

MAX_COUNT = 1000000

data = pd.read_csv(row_path, encoding='gbk', nrows=MAX_COUNT, header=None)
data.to_csv(train_1_path, index=False, header=False)
print(data)
