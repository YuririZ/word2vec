import pandas as pd
from gensim.models import word2vec
from util.word_utils import segment_sen
from util.word_utils import sent2vec
import numpy
from service.py_service import classify_message

# 文件路径
test_1_path = "D://PYTHON//data//test_data.csv"

# 读取数据
row_data = pd.read_csv(test_1_path, encoding='utf-8', header=None)
print(row_data)
data = row_data[1000000:1020000]

# 载入模型
model = word2vec.Word2Vec.load('word2vec.model')

# 构造数据
sentance = list(data[1])
labels = list(data[0])

right = 0
left = len(labels)
for sen, label in zip(sentance, labels):
    print(left)
    result = classify_message(sen)
    if result[0] == label:
        right += 1
    left -= 1
accuracy_rate = right/len(labels)
print(accuracy_rate)
