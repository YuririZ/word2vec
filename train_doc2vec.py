import random

from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import pandas as pd
import logging

from common.constant import Constant

# 读取数据
data = pd.read_csv(Constant.classification_segment_data_path_csv, encoding='utf-8', header=None)

# 构造数据
labels = data[0]
sentences = data[1]

# 分词后的结果
sens_list = []
for sen in sentences:
    if isinstance(sen, str):
        sens_list.append(sen.split(","))
    else:
        sens_list.append([str(sen)])

label_list = list(data[0])

random.seed(123)
random.shuffle(label_list)
random.seed(123)
random.shuffle(sens_list)
sens_list = sens_list[0:int(len(sens_list)*0.8)]
label_list = label_list[0:int(len(label_list)*0.8)]
documents = [TaggedDocument(doc, [label]) for doc, label in zip(sens_list, label_list)]

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
doc_model = Doc2Vec(documents, size=100, window=5, min_count=1, workers=5)
doc_model.save("doc2vec.model")
