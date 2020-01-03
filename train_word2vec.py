from gensim.models import word2vec
import pandas as pd
import logging
from util.word_utils import segment_sen

# 文件路径
all_path = "D://PYTHON//data//all_data.csv"
train_1_path = "D://PYTHON//data//train_data_1.csv"
learn_path = "D://PYTHON//data//learn_path.csv"

# 窗口大小
WIN = 5

# 读取数据
data = pd.read_csv(all_path, encoding='gbk', header=None)
# 构造数据
sentance = list(data[1])
labels = list(data[0])
# 分词后的结果
sens_list = [segment_sen(i) for i in sentance]
if len(sens_list) == len(labels):
    for sen, label in zip(sens_list, labels):
        print(sen)
        length = len(sen)
        sen.append(label)
        length -= WIN * 2
        while length > 0:
            sen.insert(length, label)
            length -= WIN * 2

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = word2vec.Word2Vec(sens_list, min_count=1, iter=20, window=WIN)
model.save("word2vec_900m.model")
