import pandas as pd

# 文件路径
train_1_path = "D://PYTHON//word2vec//data//train_data_1.csv"
learn_path = "D://PYTHON//word2vec//data//learn_path.csv"

# 窗口大小
WIN = 5

# 读取数据
data = pd.read_csv(train_1_path, encoding='utf-8', header=None, nrows=5)

print(data)